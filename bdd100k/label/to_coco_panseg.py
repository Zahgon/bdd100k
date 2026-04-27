"""Convert BDD100K bitmasks to COCO panoptic segmentation format."""

import argparse
import json
import os
from multiprocessing import Pool
from typing import Dict, List

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayI32, NDArrayU8
from scalabel.label.coco_typing import (
    ImgType,
    PanopticAnnType,
    PanopticCatType,
    PanopticGtType,
    PanopticSegType,
)
from tqdm import tqdm

from bdd100k.common.utils import list_files

from ..common.logger import logger
from .label import labels
from .to_coco import bitmasks_loader
from .to_mask import STUFF_NUM


def parse_args() -> argparse.Namespace:
    pass


def bitmask2pan_mask(mask_name: str, pan_name: str) -> None:
    pass


def bitmask2pan_json(image: ImgType, mask_name: str) -> PanopticAnnType:
    pass


def bitmask2panseg_parallel(
    mask_base: str,
    pan_mask_base: str,
    images: List[ImgType],
    nproc: int = NPROC,
) -> List[PanopticAnnType]:
    pass


def bitmask2coco_pan_seg(
    mask_base: str,
    pan_mask_base: str,
    nproc: int = NPROC,
) -> PanopticGtType:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
