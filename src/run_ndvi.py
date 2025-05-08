#!/usr/bin/env python3

from src.ndvi_processor import calc_tif_ndvi
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_ndvi.py <path_to_config.yaml>")
        sys.exit(1)

    config_path = sys.argv[1]
    calc_tif_ndvi(config_path)