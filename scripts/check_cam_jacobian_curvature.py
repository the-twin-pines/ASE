#!/usr/bin/env python3
"""Synthetic algebra/geometry checks; no measured Dakota calibration is supplied."""

from fractions import Fraction as Q
from math import cos, isclose, sin


def close(actual: float, expected: float, tolerance: float = 1e-9) -> None:
    if not isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError((actual, expected))


def determinant(matrix: list[list[float]]) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def signed_curve_curvature(velocity: tuple[float, float],
                           acceleration: tuple[float, float]) -> float:
    speed_squared = sum(value * value for value in velocity)
    if speed_squared == 0:
        raise ValueError("curve parameter is not regular")
    return (velocity[0] * acceleration[1] - velocity[1] * acceleration[0]) / speed_squared**1.5


def main() -> None:
    # General constant-camber tangent, checked in exact rational arithmetic.
    a, b, p, q = Q(2), Q(1, 3), Q(-4, 5), Q(7, 6)
    front_per_rear = -b / a
    assert a * front_per_rear + b == 0
    assert p * front_per_rear + q == (a * q - b * p) / a

    # Illustrative lower-arm geometry, not measured dimensions or service gains.
    alpha, reach, spacing, height = Q(3, 4), Q(2), Q(5), Q(7)
    j = [[-alpha / height, -(1 - alpha) / height],
         [-reach / (spacing * height), reach / (spacing * height)]]
    assert j[0][0] + j[0][1] == -1 / height
    assert j[1][0] + j[1][1] == 0
    assert determinant(j) == -reach / (spacing * height**2)

    # Nonlinear shear F(a,b)=(a,b+c*a*a): variable metric, flat full image.
    # g=[[1+4*c*c*a*a,2*c*a],[2*c*a,1]]. Its sole nonzero Christoffel
    # coefficient is Gamma^b_aa=2*c, constant; all derivative/product terms
    # of its Riemann tensor vanish. The note gives the coordinate proof.
    c = Q(2, 3)
    for a_value in (Q(-2), Q(0), Q(3, 2)):
        g = [[1 + 4*c*c*a_value*a_value, 2*c*a_value],
             [2*c*a_value, Q(1)]]
        assert determinant(g) == 1
        gamma = {(1, 0, 0): 2*c}
        for ell in range(2):
            for k in range(2):
                for i in range(2):
                    for j_index in range(2):
                        products = sum(
                            gamma.get((ell, i, m), 0) * gamma.get((m, j_index, k), 0)
                            - gamma.get((ell, j_index, m), 0) * gamma.get((m, i, k), 0)
                            for m in range(2)
                        )
                        assert products == 0
        velocity = (1.0, float(2*c*a_value))
        acceleration = (0.0, float(2*c))
        expected = float(2*c) / float(1 + 4*c*c*a_value*a_value)**1.5
        close(signed_curve_curvature(velocity, acceleration), expected)
        assert expected > 0

    # Eccentric angle can give nonzero acceleration on a straight response path.
    angle, eccentricity = 0.7, 2.0
    direction = (2.0, -3.0)
    velocity = tuple(value * -eccentricity * sin(angle) for value in direction)
    acceleration = tuple(value * -eccentricity * cos(angle) for value in direction)
    assert sum(value * value for value in acceleration) > 0
    close(signed_curve_curvature(velocity, acceleration), 0.0)
    try:
        signed_curve_curvature((0.0, 0.0), acceleration)
    except ValueError:
        pass
    else:
        raise AssertionError("a zero-speed cam turning point is not regular")

    # Counterclockwise circle with inward normal: offset Jacobian 1-r/R.
    radius, arc_length = 2.0, 0.3
    theta = arc_length / radius
    tangent = (-sin(theta), cos(theta))
    normal = (-cos(theta), -sin(theta))
    curvature = 1 / radius
    for offset in (0.0, 0.5, radius):
        scale = 1 - offset * curvature
        ds = tuple(scale * value for value in tangent)
        close(ds[0] * normal[1] - ds[1] * normal[0], scale)
    close(1 - radius * curvature, 0.0)

    # Central and mixed differences recover a quadratic response exactly.
    def response(x: Q, y: Q) -> Q:
        return 2*x + 3*y + 5*x*x + 7*x*y + 11*y*y

    x0, y0, step = Q(1, 3), Q(-1, 4), Q(1, 10)
    second_x = (response(x0+step, y0) - 2*response(x0, y0)
                + response(x0-step, y0)) / step**2
    mixed = (response(x0+step, y0+step) - response(x0+step, y0-step)
             - response(x0-step, y0+step) + response(x0-step, y0-step)) / (4*step**2)
    assert second_x == 10
    assert mixed == 7

    print("constant-camber compensation and lower-arm sketch: passed")
    print("nonlinear flat metric versus curved fixed-control path: passed")
    print("eccentric changing speed versus genuine curve curvature: passed")
    print("normal-offset tolerance band and focal singularity: passed")
    print("quadratic second/mixed finite differences: passed")
    print("synthetic mathematics only; truck Jacobian/curvature remain unmeasured")


if __name__ == "__main__":
    main()
