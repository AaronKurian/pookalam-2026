from __future__ import annotations

import math
import turtle

from geometry import polar_point, scaled
from primitives import draw_polygon


def draw_repeating_triangle_pattern(pen: turtle.Turtle, length: float, color: str, repeat_count: int) -> None:
    length = scaled(length)
    pen.color(color)
    pen.pendown()

    for _ in range(repeat_count):
        pen.begin_fill()
        pen.forward(length / math.tan(math.pi / 3.6))
        pen.left(130)
        pen.forward(length / math.sin(math.pi / 3.6))
        pen.left(100)
        pen.forward(length / math.sin(math.pi / 3.6))
        pen.left(130)
        pen.forward(length / math.tan(math.pi / 3.6))
        pen.end_fill()
        pen.left(360 / repeat_count)

    pen.left(5)
    pen.penup()


def draw_radial_triangle(
    pen: turtle.Turtle,
    angle: float,
    inner_radius: float,
    outer_radius: float,
    half_width_deg: float,
    color: str,
) -> None:
    triangle = [
        polar_point(outer_radius, angle),
        polar_point(inner_radius, angle - half_width_deg),
        polar_point(inner_radius, angle + half_width_deg),
    ]
    draw_polygon(pen, triangle, fill=color)


def draw_radial_triangle_ring(
    pen: turtle.Turtle,
    count: int,
    inner_radius: float,
    outer_radius: float,
    half_width_deg: float,
    color: str,
    start_angle: float,
) -> None:
    for i in range(count):
        angle = start_angle + i * 360 / count
        draw_radial_triangle(pen, angle, inner_radius, outer_radius, half_width_deg, color)
