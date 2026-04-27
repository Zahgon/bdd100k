"""An offline label visualizer for BDD100K file.

Works for 2D / 3D bounding box, segmentation masks, etc.
"""

import argparse
import concurrent.futures
from typing import Dict

import numpy as np
from scalabel.common.parallel import NPROC
from scalabel.common.typing import NDArrayF64
from scalabel.label.typing import Label
from scalabel.vis.controller import (
    ControllerConfig,
    DisplayConfig,
    ViewController,
)
from scalabel.vis.label import LabelViewer, UIConfig

from ..label.label import drivables, labels, lane_categories


class LabelViewerBDD100K(LabelViewer):
    """Basic class for viewing BDD100K labels."""

    def __init__(self, ui_cfg: UIConfig) -> None:
        """Initializer."""
        super().__init__(ui_cfg)
        self.colors: Dict[str, NDArrayF64] = {
            label.name: np.array(label.color)
            for label in labels
            if not label.hasInstances
        }
        self.colors.update(
            {drivable.name: np.array(drivable.color) for drivable in drivables}
        )
        self.colors.update(
            {lane.name: np.array(lane.color) for lane in lane_categories}
        )

    def _get_label_color(self, label: Label) -> NDArrayF64:
        """Get color by category and id."""
        pass


def parse_args() -> argparse.Namespace:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
