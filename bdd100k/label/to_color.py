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
    """Parse arguments."""
    parser = argparse.ArgumentParser(description="masks/bitmasks to colormaps")
    parser.add_argument(
        "-i", "--input", help="path to the directory of masks/bitmasks."
    )
    parser.add_argument(
        "-o", "--output", help="path to save generated colormaps."
    )
    parser.add_argument(
        "-m",
        "--mode",
        default="det",
        choices=[
            "sem_seg",
            "drivable",
            "lane_mark",
            "ins_seg",
            "pan_seg",
            "seg_track",
        ],
        help="conversion mode.",
    )
    parser.add_argument(
        "--nproc",
        type=int,
        default=NPROC,
        help="number of processes for conversion.",
    )
    return parser.parse_args()


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
    """Main function."""
    args = parse_args()
    colormap_func = (
        video_dataset_to_colormap
        if args.mode == "seg_track"
        else image_dataset_to_colormap
    )
    colormap_func(args.input, args.output, args.mode, args.nproc)


if __name__ == "__main__":
    main()
