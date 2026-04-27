"""BDD100K tracking evaluation with CLEAR MOT metrics."""

import os
import time
from functools import partial
from multiprocessing import Pool
from typing import List

import motmetrics as mm
import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayU8
from scalabel.eval.mot import (
    METRIC_MAPS,
    TrackResult,
    aggregate_accs,
    evaluate_single_class,
    generate_results,
)
from scalabel.label.typing import Config
from scalabel.label.utils import get_leaf_categories, get_parent_categories

from bdd100k.common.utils import reorder_preds

from ..common.bitmask import (
    bitmask_intersection_rate,
    gen_blank_bitmask,
    parse_bitmask,
)
from ..common.logger import logger

Files = List[str]
FilesList = List[Files]


def acc_single_video_mots(
    gts: Files,
    results: Files,
    classes: List[str],
    iou_thr: float = 0.5,
    ignore_iof_thr: float = 0.5,
    ignore_unknown_cats: bool = False,  # pylint: disable=unused-argument
) -> List[mm.MOTAccumulator]:
    """Accumulate results for one video."""
    pass


def evaluate_seg_track(
    gts: FilesList,
    results: FilesList,
    config: Config,
    iou_thr: float = 0.5,
    ignore_iof_thr: float = 0.5,
    nproc: int = NPROC,
) -> TrackResult:
    """Evaluate CLEAR MOT metrics for MOTS.

    Args:
        gts: the ground truth annotation files.
        results: the prediction result files.
        config: Config object
        iou_thr: Minimum IoU for a bounding box to be considered a positive.
        ignore_iof_thr: Min. Intersection over foreground with ignore regions.
        nproc: processes number for loading files

    Returns:
        TrackResult: evaluation results.
    """
    pass
