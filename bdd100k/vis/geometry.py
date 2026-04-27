# noqa
# type: ignore
# pylint: skip-file


import numpy as np


def rotate_vector(vector, rot_x=0, rot_y=0, rot_z=0, center=None):
    pass


def vector_3d_to_2d(vector, calibration):
    pass


def check_side_of_line(point, line):
    pass


def check_clockwise(points):
    pass


class Vertex:
    def __init__(self, vector, calibration):
        self.v3d = vector
        self.v2d = vector_3d_to_2d(vector, calibration)


class Label3d:
    def __init__(self, vertices):
        self.vertices = vertices

    @classmethod
    def from_box3d(cls, box3d):
        pass

    def get_edges_with_visibility(self, calibration):
        pass
