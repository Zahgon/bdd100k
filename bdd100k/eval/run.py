"""Evaluation helper functions."""

import argparse
import json
import os
from typing import List, Optional, Tuple

from scalabel.common.parallel import NPROC
from scalabel.eval.boundary import evaluate_boundary
from scalabel.eval.detect import evaluate_det
from scalabel.eval.ins_seg import evaluate_ins_seg as sc_eval_ins_seg
from scalabel.eval.mot import acc_single_video_mot, evaluate_track
from scalabel.eval.mots import acc_single_video_mots
from scalabel.eval.mots import evaluate_seg_track as sc_eval_seg_track
from scalabel.eval.pan_seg import evaluate_pan_seg as sc_eval_pan_seg
from scalabel.eval.pose import evaluate_pose
from scalabel.eval.result import Result
from scalabel.eval.sem_seg import evaluate_sem_seg as sc_eval_sem_seg
from scalabel.label.io import group_and_sort, load
from scalabel.label.typing import Frame

from bdd100k.common.utils import (
    group_and_sort_files,
    list_files,
    load_bdd100k_config,
)

from ..common.logger import logger
from ..common.typing import BDD100KConfig
from ..label.to_scalabel import bdd100k_to_scalabel
from .ins_seg import evaluate_ins_seg
from .lane import evaluate_lane_marking
from .mots import evaluate_seg_track
from .pan_seg import evaluate_pan_seg
from .seg import evaluate_drivable, evaluate_sem_seg


def parse_args() -> argparse.Namespace:
    pass


def run_bitmask(
    config: BDD100KConfig,
    task: str,
    gt_paths: List[str],
    pred_paths: List[str],
    score_file: Optional[str],
    iou_thr: float = 0.5,
    ignore_iof_thr: float = 0.5,
    quiet: bool = False,
    nproc: int = NPROC,
) -> Result:
    pass


def run_rle(
    config: BDD100KConfig,
    task: str,
    gt_frames: List[Frame],
    pred_frames: List[Frame],
    iou_thr: float = 0.5,
    ignore_iof_thr: float = 0.5,
    nproc: int = NPROC,
) -> Result:
    pass


def _load_frames(
    gt_base: str, result_path: str, config: BDD100KConfig, nproc: int = NPROC
) -> Tuple[List[Frame], List[Frame]]:
    pass


def run() -> None:
    pass


if __name__ == "__main__":
    run()
