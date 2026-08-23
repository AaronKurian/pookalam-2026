from __future__ import annotations

import math
import turtle

from primitives import draw_polygon


def draw_radial_ellipse(
    pen: turtle.Turtle,
    center_x: float,
    center_y: float,
    radius: float,
    stretch_factor: float,
    unit_x: float,
    unit_y: float,
    color: str,
) -> None:
    points = []

    for angle_step in range(37):
        angle = math.radians(angle_step * 10)
        local_x = radius * math.cos(angle) * stretch_factor
        local_y = radius * math.sin(angle)
        rotated_x = local_x * unit_x - local_y * unit_y
        rotated_y = local_x * unit_y + local_y * unit_x
        points.append((center_x + rotated_x, center_y + rotated_y))

    draw_polygon(pen, points, fill=color, outline=color)
