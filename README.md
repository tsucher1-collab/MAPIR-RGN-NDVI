# MAPIR RGN NDVI Processor

This repository contains a script to calculate the NDVI (Normalized Difference Vegetation Index) from MAPIR RGN images using Python. It leverages `rasterio` for raster file handling, `numpy` for numerical operations, and other common Python libraries to process remote sensing imagery.

## Requirements

Before running the script, ensure that you have the following installed:

- Python 3.x
- pip
- [Git](https://git-scm.com/)
- [Git LFS](https://git-lfs.github.com/) (if working with large files)
- Required Python packages (listed below)

### Install Dependencies

1. Clone this repository:
   ```bash
   
   git clone https://github.com/your-username/MAPIR-RGN-NDVI.git
   cd MAPIR-RGN-NDVI

2. Set up a Python virtual environment (optional but recommended):
   ```bash
   
   python3 -m venv mapir_env
   source mapir_env/bin/activate  # On Windows use `mapir_env\Scripts\activate`
3. Install the necessary Python libraries:
   ```bash
   
   cd src
   pip install -r requirements.txt

### Configuration File

The configuration file (config/ndvi_conf.yaml) contains paths for the input image and the output NDVI raster. You will need to modify this file to suit your environment.

1. Example CONFIG Format:
  ```bash

  input_path: data/mapir_image.tif
  output_path: output/ndvi_rasterio.tif
```

### Recommended Directory Structure


- **`MAPIR-RGN_NDVI/`**
  - **`data/`**: Store your input `.tif` files here. For example, `mapir_image.tif`.
  - **`output/`**: This folder will contain the resulting NDVI raster files.
  - **`config/`**: Contains configuration files, such as `ndvi_conf.yaml`, for specifying input/output paths.
  - **`src/`**: Contains all source code, including:
    - `requirements.txt` – Python dependencies
    - `ndvi_processor.py` – The core processing logic for calculating NDVI
    - `NDVI.ipynb` – Jupyter notebook for debugging the code
    - `run_ndvi.py` – The script to run NDVI processing
  - **`mapir_env/`**: The virtual environment where dependencies are installed. Its contents are not listed here.
  - **`.gitignore`**: Specifies which files and directories should be ignored by Git (e.g., `mapir_env/`).

---


### Running the Script

1. Activate virtual environment (if necessary):
   ```bash

   source mapir_env/bin/activate
   ```
2. Run the NDVI activation function using python (from project folder):
   ```bash

   python -m src.run_ndvi config/ndvi_conf.yaml
   ```

NOTE: Output NDVI geotiff will be saved to the specified path in ndvi_conf.yaml. Large images may take time to process.



