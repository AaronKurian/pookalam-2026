from __future__ import annotations

import turtle

from geometry import polar_point
from primitives import draw_polygon


def draw_pentagon_unit(pen: turtle.Turtle, angle: float) -> list[tuple[float, float]]:
    outer_radius = 620
    shoulder_radius = 526
    inner_radius = 403
    half_width = 14

    pentagon = [
        polar_point(outer_radius, angle),
        polar_point(shoulder_radius, angle + 18),
        polar_point(inner_radius, angle + half_width),
        polar_point(inner_radius, angle - half_width),
        polar_point(shoulder_radius, angle - 18),
    ]
    draw_polygon(pen, pentagon, fill="#ffd400")

    triangle = [pentagon[0], pentagon[2], pentagon[3]]
    draw_polygon(pen, triangle, fill="#ff7a00")
    return pentagon


def draw_pentagon_triangle_pattern(pen: turtle.Turtle) -> None:
    count = 8
    angle_step = 360 / count
    units = [draw_pentagon_unit(pen, i * angle_step - 90) for i in range(count)]

    for i in range(count):
        current_right_shoulder = units[i][1]
        next_left_shoulder = units[(i + 1) % count][4]
        gap_angle = i * angle_step - 90 + angle_step / 2
        inner_left = units[i][2]
        inner_right = units[(i + 1) % count][3]
        draw_polygon(
            pen,
            [current_right_shoulder, next_left_shoulder, inner_right, inner_left],
            fill="#fff8dc",
            outline="#fff8dc",
            width=3,
        )
        triangle = [
            current_right_shoulder,
            next_left_shoulder,
            polar_point(620, gap_angle),
        ]
        draw_polygon(pen, triangle, fill="#fff8dc", outline="#fff8dc", width=3)
