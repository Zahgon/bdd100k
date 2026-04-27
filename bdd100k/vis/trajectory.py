"""Visualize GPS trajectory.

To install the gmplot package, call:

    pip install gmplot

To create a Google Map API key, please follow the instruction below:

    https://developers.google.com/maps/documentation/embed/get-api-key
"""

import argparse
import json
import os
from glob import glob

import gmplot
import numpy as np
from scalabel.common.typing import NDArrayF64

from ..common.logger import logger


def visualize_file(in_file: str, out_file: str, apikey: str) -> None:
    """Visualize one GPS file.

    Given a input json file with gps trajectory and the Google Map API Key,
    creates an html that displays the given trajectory.

    Arguments:
        in_file:  source json file
        out_file: path to save output html
        apikey:   Google Map API key
    """
    # open info json
    pass


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
    pass


def main() -> None:
    """Main."""
    pass


if __name__ == "__main__":
    main()
