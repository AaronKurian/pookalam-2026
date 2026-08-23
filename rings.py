from __future__ import annotations

import math
import turtle

from circles import draw_circle_at, draw_nested_circle_at
from geometry import polar_point, scaled


def draw_patch_ring(
    pen: turtle.Turtle,
    radius: float,
    patch_radius: float,
    count: int,
    colors: list[str],
    start_angle: float = -90,
) -> None:
    for i in range(count):
        angle = start_angle + i * 360 / count
        draw_circle_at(pen, polar_point(radius, angle), patch_radius, colors[i % len(colors)])


def draw_nested_circle_ring(
    pen: turtle.Turtle,
    big_radius: float,
    small_radius: float,
    count: int,
    colors: list[str],
    start_angle: float = 0,
) -> None:
    ring_radius = scaled(big_radius - small_radius)
    for i in range(count):
        angle = math.radians(start_angle + i * 360 / count)
        center = (ring_radius * math.cos(angle), ring_radius * math.sin(angle))
        draw_nested_circle_at(pen, center, small_radius, colors)


def draw_paired_small_circles_ring(
    pen: turtle.Turtle,
    big_radius: float,
    small_radius: float,
    pair_count: int,
    colors: list[str],
    pair_gap_degrees: float,
    start_angle: float = 0,
) -> None:
    ring_radius = scaled(big_radius - small_radius)
    for i in range(pair_count):
        center_angle = start_angle + i * 360 / pair_count
        for dot_offset in (-pair_gap_degrees / 2, pair_gap_degrees / 2):
            angle = math.radians(center_angle + dot_offset)
            center = (ring_radius * math.cos(angle), ring_radius * math.sin(angle))
            draw_nested_circle_at(pen, center, small_radius, colors)

    pen.penup()
