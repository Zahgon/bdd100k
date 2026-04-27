"""Support functions for Bitmask."""

from typing import List, Tuple

import numpy as np
from scalabel.common.typing import NDArrayF64, NDArrayI32, NDArrayU8

MAX_DET = 100


def gen_blank_bitmask(shape: Tuple[int, ...]) -> NDArrayU8:
    """Generate blank bitmask given the shape."""
    pass


def parse_bitmask(
    bitmask: NDArrayU8, stacked: bool = False
) -> List[NDArrayI32]:
    """Parse information from bitmasks and compress its value range.

    The compression works like: [4, 2, 9] --> [2, 1, 3]
    """
    pass


def bitmask_intersection_rate(
    gt_masks: NDArrayI32, pred_masks: NDArrayI32
) -> Tuple[NDArrayF64, NDArrayF64]:
    """Returns the intersection over the area of the predicted box."""
    pass
