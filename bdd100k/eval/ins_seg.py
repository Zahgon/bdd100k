"""Evaluation code for BDD100K instance segmentation.

predictions format: BitMasks
"""

import copy
import json
import os
from multiprocessing import Pool
from typing import Dict, List, Tuple

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import (
    DictStrAny,
    NDArrayF64,
    NDArrayI32,
    NDArrayU8,
)
from scalabel.eval.detect import COCOevalV2, DetResult
from scalabel.label.transforms import get_coco_categories
from scalabel.label.typing import Config
from tqdm import tqdm

from bdd100k.common.utils import reorder_preds

from ..common.bitmask import bitmask_intersection_rate, parse_bitmask
from ..common.logger import logger


def parse_res_bitmask(
    ann_score: List[Tuple[int, float]], bitmask: NDArrayU8
) -> List[NDArrayI32]:
    """Parse information from result bitmasks and compress its value range."""
    bitmask = bitmask.astype(np.int32)
    category_map = bitmask[:, :, 0]
    ann_map = (bitmask[:, :, 2] << 8) + bitmask[:, :, 3]

    ann_ids = []
    scores = []
    category_ids = []

    masks: NDArrayI32 = np.zeros(bitmask.shape[:2], dtype=np.int32)
    i = 0
    ann_score = sorted(ann_score, key=lambda pair: pair[1], reverse=True)
    for ann_id, score in ann_score:
        mask_inds_i = ann_map == ann_id
        if np.count_nonzero(mask_inds_i) == 0:
            continue

        # 0 is for the background
        i += 1
        masks[mask_inds_i] = i
        ann_ids.append(i)
        scores.append(score)

        category_ids_i: NDArrayI32 = np.unique(category_map[mask_inds_i])
        assert category_ids_i.shape[0] == 1
        category_ids.append(category_ids_i[0])

    return [masks, np.array(ann_ids), np.array(scores), np.array(category_ids)]


def get_mask_areas(masks: NDArrayI32) -> NDArrayF64:
    """Get mask areas from the compressed mask map."""
    pass


class BDD100KInsSegEval(COCOevalV2):
    """Modify the COCO API to support bitmasks as input."""

    def __init__(
        self,
        gt_paths: List[str],
        dt_paths: List[str],
        dt_json: str,
        cat_names: List[str],
        nproc: int = NPROC,
    ) -> None:
        """Initialize InsSeg eval."""
        super().__init__(cat_names)
        self.gt_paths = {os.path.basename(p): p for p in gt_paths}
        self.dt_paths = {os.path.basename(p): p for p in dt_paths}
        self.dt_json = dt_json
        self.nproc = nproc
        self.img_names: List[str] = []
        self.img2score: Dict[str, List[Tuple[int, float]]] = {}
        self.evalImgs: List[DictStrAny] = []
        self.iou_res: List[DictStrAny] = []

        self._prepare()

    def __len__(self) -> int:
        """Get image number."""
        return len(self.img_names)

    def _prepare(self) -> None:
        """Prepare file list for evaluation."""
        pass

    def evaluate(self) -> None:
        """Run per image evaluation."""
        p = self.params
        p.maxDets = sorted(p.maxDets)
        self.params = p

        # loop through images, area range, max detection number
        if self.nproc > 1:
            with Pool(self.nproc) as pool:
                to_updates: List[Dict[int, DictStrAny]] = pool.map(
                    self.compute_match, range(len(self))
                )
        else:
            to_updates = list(map(self.compute_match, range(len(self))))

        eval_num = len(p.catIds) * len(p.areaRng) * len(self)
        self.evalImgs = [{} for _ in range(eval_num)]
        for to_update in to_updates:
            for ind, item in to_update.items():
                self.evalImgs[ind].update(item)

        self._paramsEval = copy.deepcopy(self.params)

    def compute_iou(self, img_ind: int) -> DictStrAny:
        """Compute IoU per image."""
        pass

    def compute_match(self, img_ind: int) -> Dict[int, DictStrAny]:
        """Compute matching results for each image."""
        pass


def evaluate_ins_seg(
    gt_paths: List[str],
    pred_paths: List[str],
    pred_score_file: str,
    config: Config,
    nproc: int = NPROC,
    with_logs: bool = True,
) -> DetResult:
    """Load the ground truth and prediction results.

    Args:
        gt_paths: paths to the ground truth bitmasks.
        pred_paths: paths to the prediciton bitmasks.
        pred_score_file: path tothe prediction scores.
        config: Config instance.
        nproc: number of processes.
        with_logs: whether to print logs

    Returns:
        dict: detection metric scores
    """
    categories = get_coco_categories(config)
    cat_ids = [category["id"] for category in categories]
    cat_names = [category["name"] for category in categories]
    pred_paths = reorder_preds(gt_paths, pred_paths)
    bdd_eval = BDD100KInsSegEval(
        gt_paths, pred_paths, pred_score_file, cat_names, nproc
    )
    bdd_eval.params.catIds = cat_ids
    if with_logs:
        logger.info("evaluating...")
    bdd_eval.evaluate()
    if with_logs:
        logger.info("accumulating...")
    bdd_eval.accumulate()
    result = bdd_eval.summarize()  # pylint: disable=redefined-outer-name
    return result
