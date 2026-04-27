"""Run data commands in parallel."""

from __future__ import annotations

import argparse
import os
from os.path import dirname, join, splitext
from subprocess import DEVNULL, check_call
from typing import Callable, List

from joblib import Parallel, delayed
from tqdm import tqdm


def parse_arguments() -> argparse.Namespace:
    pass


def copy(src: str, target: str) -> None:
    pass


def zipdir(src: str, target: str) -> None:
    """Zip the src folder."""
    pass


def unzip(src: str, target: str) -> None:
    """Unzip the src folder."""
    pass


def create_subpath(filepath: str) -> str:
    pass


def listdir(in_dir: str) -> List[str]:
    pass


def run() -> None:
    pass


if __name__ == "__main__":
    run()
