"""Generate palettes for different tasks."""

from typing import Dict, List

import numpy as np

from .label import drivables, labels, lane_categories
from .to_mask import STUFF_NUM

PALETTES: Dict[str, List[int]] = {}


def get_palette(mode: str) -> List[int]:
    pass
