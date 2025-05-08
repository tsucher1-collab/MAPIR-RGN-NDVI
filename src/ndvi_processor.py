import rasterio
import numpy as np
import time
from threading import Thread, Event
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def compute_ndvi(red, nir):
    with np.errstate(divide='ignore', invalid='ignore'):
        ndvi = (nir - red) / (nir + red)
        ndvi = np.where((nir + red) == 0, 0, ndvi)
        return np.clip(ndvi, -1, 1)

def calc_tif_ndvi(config_path):
    config = load_config(config_path)
    fp = config['input_path']
    output_path = config['output_path']

    print("NDVI processing underway.")
    processing_done = Event()

    def print_progress():
        start_time = time.time()
        last_report = 0
        while not processing_done.is_set():
            elapsed = time.time() - start_time
            if elapsed >= last_report + 10:
                print(f"Processing... {int(elapsed//10)*10} seconds elapsed")
                last_report = elapsed//10 * 10
            time.sleep(0.1)
    
    progress_thread = Thread(target=print_progress)
    progress_thread.start()

    try:
        with rasterio.open(fp) as src:
            red = src.read(1).astype(float) / 10000
            nir = src.read(3).astype(float) / 10000
            ndvi = compute_ndvi(red, nir)

            profile = src.profile
            profile.update(
                dtype=rasterio.float32,
                count=1,
                nodata=np.nan,
                driver='GTiff'
            )

            with rasterio.open(output_path, 'w', **profile) as dst:
                dst.write(ndvi.astype(rasterio.float32), 1)
                dst.set_band_description(1, 'NDVI')

        print("NDVI range:", np.nanmin(ndvi), np.nanmax(ndvi))
        print(f"NDVI processing finished! Result saved to {output_path}")

    finally:
        processing_done.set()
        progress_thread.join()