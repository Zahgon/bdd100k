"""Generate the image lists for data loaders."""

import os
import sys
from os import path as osp

from ..common.logger import logger


def gen_list(
    data_root: str,
    data_dir: str,
    list_dir: str,
    phase: str,
    list_type: str,
    suffix: str = ".jpg",
) -> None:
    pass


def gen_images(
    data_root: str, list_dir: str, image_type: str = "100k"
) -> None:
    pass


def gen_drivable(data_root: str) -> None:
    pass


def gen_seg(data_root: str) -> None:
    pass


if __name__ == "__main__":
    gen_drivable(sys.argv[1])
    gen_seg(sys.argv[1])
