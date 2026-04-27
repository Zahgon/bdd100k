"""Util functions."""

import os
import os.path as osp
from itertools import groupby
from typing import Dict, List, Tuple

from scalabel.common.io import load_config
from scalabel.label.to_coco import get_instance_id
from scalabel.label.typing import Label
from scalabel.label.utils import check_crowd, check_ignored

from .logger import logger
from .typing import BDD100KConfig


def list_files(
    inputs: str, suffix: str = "", with_prefix: bool = False
) -> List[str]:
    pass


def group_and_sort_files(files: List[str]) -> List[List[str]]:
    pass


def get_bdd100k_instance_id(
    instance_id_maps: Dict[str, int], global_instance_id: int, scalabel_id: str
) -> Tuple[int, int]:
    pass


def check_bdd100k_crowd(label: Label) -> bool:
    """Check crowd attribute for BDD100K."""
    pass


def check_bdd100k_ignored(label: Label) -> bool:
    """Check ignored attribute for BDD100K."""
    pass


def load_bdd100k_config(cfg_path: str) -> BDD100KConfig:
    pass


def reorder_preds(gt_paths: List[str], pred_paths: List[str]) -> List[str]:
    pass
