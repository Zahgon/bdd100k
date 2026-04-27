"""Convert poly2d to mask/bitmask."""

import os
from functools import partial
from multiprocessing import Pool
from typing import Callable, Dict, List

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayU8
from scalabel.label.io import group_and_sort, load
from scalabel.label.transforms import poly_to_patch
from scalabel.label.typing import Config, Frame, ImageSize, Label, Poly2D
from scalabel.label.utils import (
    check_crowd,
    check_ignored,
    get_leaf_categories,
)
from tqdm import tqdm

from bdd100k.common.utils import get_bdd100k_instance_id, load_bdd100k_config

from ..common.logger import logger
from ..common.typing import BDD100KConfig
from .label import drivables, labels, lane_categories
from .to_coco import parse_args
from .to_scalabel import bdd100k_to_scalabel

IGNORE_LABEL = 255
STUFF_NUM = 30
LANE_DIRECTION_MAP = {"parallel": 0, "vertical": 1}
LANE_STYLE_MAP = {"solid": 0, "dashed": 1}


def frame_to_mask(
    out_path: str,
    shape: ImageSize,
    colors: List[NDArrayU8],
    poly2ds: List[List[Poly2D]],
    with_instances: bool = True,
    back_color: int = 0,
    closed: bool = True,
) -> None:
    """Converting a frame of poly2ds to mask/bitmask."""
    pass


def set_instance_color(
    label: Label, category_id: int, ann_id: int
) -> NDArrayU8:
    pass


def set_lane_color(label: Label, category_id: int) -> NDArrayU8:
    """Set the color for the lane given its attributes and category."""
    pass


def frames_to_masks(
    nproc: int,
    out_paths: List[str],
    shapes: List[ImageSize],
    colors_list: List[List[NDArrayU8]],
    poly2ds_list: List[List[List[Poly2D]]],
    with_instances: bool = True,
    back_color: int = 0,
    closed: bool = True,
) -> None:
    pass


def seg_to_masks(
    frames: List[Frame],
    out_base: str,
    config: Config,
    nproc: int = NPROC,
    mode: str = "sem_seg",
    back_color: int = IGNORE_LABEL,
    closed: bool = True,
) -> None:
    """Converting segmentation poly2d to 1-channel masks."""
    pass


ToMasksFunc = Callable[[List[Frame], str, Config, int], None]
semseg_to_masks: ToMasksFunc = partial(
    seg_to_masks, mode="sem_seg", back_color=IGNORE_LABEL, closed=True
)
drivable_to_masks: ToMasksFunc = partial(
    seg_to_masks,
    mode="drivable",
    back_color=len(drivables) - 1,
    closed=True,
)
lanemark_to_masks: ToMasksFunc = partial(
    seg_to_masks, mode="lane_mark", back_color=IGNORE_LABEL, closed=False
)


def insseg_to_bitmasks(
    frames: List[Frame], out_base: str, config: Config, nproc: int = NPROC
) -> None:
    pass


def panseg_to_bitmasks(
    frames: List[Frame], out_base: str, config: Config, nproc: int = NPROC
) -> None:
    pass


def segtrack_to_bitmasks(
    frames: List[Frame], out_base: str, config: Config, nproc: int = NPROC
) -> None:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
