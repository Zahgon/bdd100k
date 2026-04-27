"""Convert BDD100K to COCO format."""

import argparse
import json
import os
from functools import partial
from multiprocessing import Pool
from typing import Dict, List, Tuple

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayI32
from scalabel.label.coco_typing import AnnType, GtType, ImgType, VidType
from scalabel.label.io import group_and_sort, load
from scalabel.label.to_coco import (
    scalabel2coco_box_track,
    scalabel2coco_detection,
    scalabel2coco_ins_seg,
    scalabel2coco_pose,
    scalabel2coco_seg_track,
    set_seg_object_geometry,
)
from scalabel.label.transforms import get_coco_categories, mask_to_bbox
from scalabel.label.typing import Config, Frame, ImageSize
from scalabel.label.utils import (
    check_crowd,
    check_ignored,
    get_leaf_categories,
)
from tqdm import tqdm

from bdd100k.common.utils import (
    get_bdd100k_instance_id,
    group_and_sort_files,
    list_files,
    load_bdd100k_config,
)

from ..common.logger import logger
from ..common.typing import BDD100KConfig, InstanceType
from .to_scalabel import bdd100k_to_scalabel


def parse_args() -> argparse.Namespace:
    pass


def bitmasks_loader(mask_name: str) -> Tuple[List[InstanceType], ImageSize]:
    pass


def bitmask2coco_wo_ids(image: ImgType, mask_base: str) -> List[AnnType]:
    """Convert bitmasks annotations of an image to RLEs or polygons."""
    pass


def bitmask2coco_wo_ids_parallel(
    mask_base: str, images: List[ImgType], nproc: int = NPROC
) -> List[AnnType]:
    pass


def bitmask2coco_with_ids(
    annotations: List[AnnType],
    mask_name: str,
    category_ids: List[int],
    instance_ids: List[int],
) -> List[AnnType]:
    """Convert bitmasks annotations of an image to RLEs or polygons."""
    pass


def bitmask2coco_with_ids_parallel(
    annotations_list: List[List[AnnType]],
    mask_names: List[str],
    category_ids_list: List[List[int]],
    instance_ids_list: List[List[int]],
    nproc: int = NPROC,
) -> List[AnnType]:
    """Execute the bitmask conversion in parallel."""
    pass


def bitmask2coco_ins_seg(
    mask_base: str, config: Config, nproc: int = NPROC
) -> GtType:
    pass


def bitmask2coco_seg_track(
    mask_base: str, config: Config, nproc: int = NPROC
) -> GtType:
    pass


def bdd100k2coco_ins_seg(
    mask_base: str, frames: List[Frame], config: Config, nproc: int = NPROC
) -> GtType:
    """Converting BDD100K Instance Segmentation Set to COCO format."""
    pass


def bdd100k2coco_seg_track(
    mask_base: str, frames: List[Frame], config: Config, nproc: int = NPROC
) -> GtType:
    """Converting BDD100K Segmentation Tracking Set to COCO format."""
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
