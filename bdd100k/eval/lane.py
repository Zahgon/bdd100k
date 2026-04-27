"""Evaluation code for BDD100K lane marking.

************************************
Byte structure for lane marking:
+---+---+---+---+---+---+---+---+
| - | - | d | s | b | c | c | c |
+---+---+---+---+---+---+---+---+

d: direction
s: style
b: background
c: category

More details: bdd100k.label.label.py
************************************


Code adapted from:
https://github.com/fperazzi/davis/blob/master/python/lib/davis/measures/f_boundary.py

Source License

BSD 3-Clause License

Copyright (c) 2017,
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.s
############################################################################

Based on:
----------------------------------------------------------------------------
A Benchmark Dataset and Evaluation Methodology for Video Object Segmentation
Copyright (c) 2016 Federico Perazzi
Licensed under the BSD License [see LICENSE for details]
Written by Federico Perazzi
----------------------------------------------------------------------------
"""

from functools import partial
from multiprocessing import Pool
from typing import AbstractSet, Callable, Dict, List, Optional, Union

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayF64, NDArrayU8
from scalabel.eval.result import AVERAGE, Result, Scores, ScoresList
from skimage.morphology import binary_dilation, disk
from tqdm import tqdm

from bdd100k.common.utils import reorder_preds

from ..common.logger import logger
from ..label.label import lane_categories, lane_directions, lane_styles

BOUND_PIXELS = [1, 2, 5]


def eval_lane_per_threshold(
    gt_mask: NDArrayU8, pd_mask: NDArrayU8, bound_pix: int
) -> float:
    pass


def get_lane_class(
    byte: NDArrayU8, value: int, offset: int, width: int
) -> NDArrayU8:
    pass


def lane_class_func(
    offset: int, width: int
) -> Callable[[NDArrayU8, int], NDArrayU8]:
    pass


get_foreground = partial(get_lane_class, value=0, offset=3, width=1)
sub_task_funcs = {
    "direction": lane_class_func(5, 1),
    "style": lane_class_func(4, 1),
    "category": lane_class_func(0, 3),
}
sub_task_cats: Dict[str, List[str]] = {
    "direction": [label.name for label in lane_directions],
    "style": [label.name for label in lane_styles],
    "category": [label.name for label in lane_categories],
}


class LaneResult(Result):
    """The class for lane marking evaluation results."""

    F1_pix1: List[Dict[str, float]]
    F1_pix2: List[Dict[str, float]]
    F1_pix5: List[Dict[str, float]]

    # pylint: disable=useless-super-delegation
    def __eq__(self, other: "LaneResult") -> bool:  # type: ignore
        """Check whether two instances are equal."""
        return super().__eq__(other)

    def summary(
        self,
        include: Optional[AbstractSet[str]] = None,
        exclude: Optional[AbstractSet[str]] = None,
    ) -> Scores:
        """Convert the lane_mark data into a flattened dict as the summary."""
        pass


def eval_lane_per_frame(gt_path: str, pred_path: str) -> Dict[str, NDArrayF64]:
    pass


def merge_results(
    task2arr_list: List[Dict[str, NDArrayF64]]
) -> Dict[str, NDArrayF64]:
    pass


def generate_results(task2arr: Dict[str, NDArrayF64]) -> LaneResult:
    pass


def evaluate_lane_marking(
    gt_paths: List[str],
    pred_paths: List[str],
    nproc: int = NPROC,
    with_logs: bool = True,
) -> LaneResult:
    pass
