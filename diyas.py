from __future__ import annotations

import math
import turtle

from geometry import scaled
from ellipses import draw_radial_ellipse


def draw_diya_flames(
    pen: turtle.Turtle,
    x: float,
    y: float,
    center_x: float,
    center_y: float,
    radius: float,
    flame_colors: list[str],
    flame_count: int,
) -> None:
    dx = x - center_x
    dy = y - center_y
    distance = math.hypot(dx, dy)
    unit_x, unit_y = (dx / distance, dy / distance) if distance else (0, -1)

    shift_distance = radius * 1.2
    flame_start_x = x + unit_x * shift_distance
    flame_start_y = y + unit_y * shift_distance

    for flame_index in range(flame_count):
        flame_radius = radius * (flame_count - flame_index) / (flame_count + 1)
        flame_x = flame_start_x - unit_x * flame_radius
        flame_y = flame_start_y - unit_y * flame_radius
        stretch_factor = 1 + flame_index * 0.4
        color = flame_colors[flame_index] if flame_index < len(flame_colors) else flame_colors[-1]
        draw_radial_ellipse(pen, flame_x, flame_y, flame_radius, stretch_factor, unit_x, unit_y, color)


def draw_single_diya(
    pen: turtle.Turtle,
    x: float,
    y: float,
    center_x: float,
    center_y: float,
    diya_radius: float,
    diya_color: str,
    flame_colors: list[str],
    flame_count: int,
) -> None:
    dx = x - center_x
    dy = y - center_y
    distance = math.hypot(dx, dy)
    unit_x, unit_y = (dx / distance, dy / distance) if distance else (0, -1)
    draw_radial_ellipse(pen, x, y, diya_radius, 1.0, unit_x, unit_y, diya_color)
    draw_diya_flames(pen, x, y, center_x, center_y, diya_radius, flame_colors, flame_count)


def draw_diyas_around_pookalam(
    pen: turtle.Turtle,
    pookalam_radius: float = 955,
    diya_radius: float = 25,
    diya_count: int = 8,
    diya_color: str = "#582f0e",
    flame_colors: list[str] | None = None,
    flame_count: int = 4,
    start_angle: float = 0,
) -> None:
    colors = flame_colors or ["#260701", "#ffb20f", "#ffe548"]
    ring_radius = scaled(pookalam_radius - diya_radius)
    radius = scaled(diya_radius)

    for i in range(diya_count):
        angle = math.radians(start_angle + i * 360 / diya_count)
        x = ring_radius * math.cos(angle)
        y = ring_radius * math.sin(angle)
        draw_single_diya(pen, x, y, 0, 0, radius, diya_color, colors, flame_count)
