"""Convert poly2d to mask/bitmask."""

import argparse
import os
from functools import partial
from multiprocessing import Pool
from typing import List

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from tqdm import tqdm

from bdd100k.common.utils import group_and_sort_files, list_files

from ..common.logger import logger
from .palette import get_palette


def parse_args() -> argparse.Namespace:
    pass


def mask_to_color(bitmask_file: str, colormap_file: str, mode: str) -> None:
    """Convert mask/bitmask to colormap for one image."""
    pass


def masks_to_colors(
    bitmasks_files: List[str],
    colormap_files: List[str],
    mode: str,
    nproc: int = NPROC,
) -> None:
    """Convert mask/bitmask to colormap for a list of images."""
    pass


def image_dataset_to_colormap(
    in_base: str,
    out_base: str,
    mode: str,
    nproc: int = NPROC,
) -> None:
    """Convert instance segmentation bitmasks to labelmap."""
    pass


def video_dataset_to_colormap(
    in_base: str,
    out_base: str,
    mode: str,
    nproc: int = NPROC,
) -> None:
    """Convert segmentation tracking bitmasks to labelmap."""
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
