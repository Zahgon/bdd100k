"""Convert mask/bitmask to RLE."""

import argparse
import os
from functools import partial
from multiprocessing import Pool
from typing import Callable, Dict, List, Tuple

import numpy as np
from PIL import Image
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayU8
from scalabel.label.io import load, save
from scalabel.label.transforms import mask_to_rle
from scalabel.label.typing import Category, Frame, Label
from scalabel.label.utils import get_leaf_categories
from tqdm import tqdm

from bdd100k.common.utils import list_files, load_bdd100k_config

from ..common.bitmask import parse_bitmask
from ..common.typing import BDD100KConfig
from ..eval.ins_seg import parse_res_bitmask

ToRLEFunc = Callable[[Frame, str, List[Category]], Frame]


def parse_args() -> argparse.Namespace:
    pass


def insseg_to_rle(
    frame: Frame, input_dir: str, categories: List[Category]
) -> Frame:
    pass


def semseg_to_rle(
    frame: Frame, input_dir: str, categories: List[Category]
) -> Frame:
    pass


def segtrack_to_rle(
    frame: Frame, input_dir: str, categories: List[Category]
) -> Frame:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
