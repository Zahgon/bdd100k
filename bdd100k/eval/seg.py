"""Evaluation procedures for semantic segmentation.

For dataset with `n` classes, we treat the index `n` as the ignored class.
When compute IoUs, this ignored class is considered.
However, IoU(ignored) doesn't influence mIoU.
"""

from functools import partial
from multiprocessing import Pool
from typing import AbstractSet, Dict, List, Optional, Set, Tuple, Union, cast

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayF64, NDArrayI32, NDArrayU8
from scalabel.eval.result import AVERAGE, Result, Scores
from tqdm import tqdm

from bdd100k.common.utils import reorder_preds

from ..common.logger import logger
from ..common.typing import NDArrayI64
from ..label.label import drivables, labels
from ..label.to_mask import IGNORE_LABEL


class SegResult(Result):
    """The class for general segmentation evaluation results."""

    IoU: List[Dict[str, float]]
    Acc: List[Dict[str, float]]
    fIoU: float
    pAcc: float

    # pylint: disable=useless-super-delegation
    def __eq__(self, other: "SegResult") -> bool:  # type: ignore
        """Check whether two instances are equal."""
        return super().__eq__(other)

    def summary(
        self,
        include: Optional[AbstractSet[str]] = None,
        exclude: Optional[AbstractSet[str]] = None,
    ) -> Scores:
        """Convert the seg result into a flattened dict as the summary."""
        pass


def fast_hist(
    groundtruth: NDArrayU8,
    prediction: NDArrayU8,
    size: int,
) -> NDArrayI64:
    pass


def per_class_iou(hist: NDArrayI32) -> NDArrayF64:
    pass


def per_class_acc(hist: NDArrayI32) -> NDArrayF64:
    pass


def whole_acc(hist: NDArrayI32) -> float:
    pass


def freq_iou(hist: NDArrayI32) -> float:
    pass


def per_image_hist(
    gt_path: str, pred_path: str = "", num_classes: int = 2
) -> Tuple[NDArrayI64, Set[int]]:
    pass


def evaluate_segmentation(
    gt_paths: List[str],
    pred_paths: List[str],
    mode: str = "sem_seg",
    nproc: int = NPROC,
    with_logs: bool = True,
) -> SegResult:
    pass


def evaluate_drivable(
    gt_paths: List[str],
    pred_paths: List[str],
    nproc: int = NPROC,
    with_logs: bool = True,
) -> SegResult:
    pass


def evaluate_sem_seg(
    gt_paths: List[str],
    pred_paths: List[str],
    nproc: int = NPROC,
    with_logs: bool = True,
) -> SegResult:
    pass
