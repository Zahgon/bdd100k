"""Convert coco to bdd100k format."""

import argparse

from scalabel.common.parallel import NPROC
from scalabel.label.from_coco import run


def parse_arguments() -> argparse.Namespace:
    pass


if __name__ == "__main__":
    run(parse_arguments())
