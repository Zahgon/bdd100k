"""Convert BDD100K to Scalabel format."""

from typing import Dict, List, Optional

from scalabel.label.typing import Frame, Label
from scalabel.label.utils import get_leaf_categories
from tqdm import tqdm

from ..common.typing import BDD100KConfig

IGNORED = "ignored"


def deal_bdd100k_category(
    label: Label, bdd100k_config: BDD100KConfig, cat_name2id: Dict[str, int]
) -> Optional[Label]:
    pass


def bdd100k_to_scalabel(
    frames: List[Frame], bdd100k_config: BDD100KConfig
) -> List[Frame]:
    pass
