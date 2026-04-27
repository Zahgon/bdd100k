"""Convert COCO panoptic segmentation format from BDD100K bitmasks."""

import argparse
import json
import os
from functools import partial
from multiprocessing import Pool

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayI32, NDArrayU8
from scalabel.label.coco_typing import PanopticAnnType, PanopticGtType
from tqdm import tqdm

from ..common.logger import logger


def parse_args() -> argparse.Namespace:
    pass


def panseg2bitmask(
    annotation: PanopticAnnType, pan_mask_base: str, mask_base: str
) -> None:
    pass


def coco_pan_seg2bitmask(
    coco_pan_seg: PanopticGtType,
    pan_mask_base: str,
    mask_base: str,
    nproc: int = NPROC,
) -> None:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
