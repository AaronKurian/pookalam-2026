from __future__ import annotations

import turtle

from circles import draw_circle
from patterns import draw_radial_triangle_ring, draw_repeating_triangle_pattern
from rings import (
    draw_nested_circle_ring,
    draw_paired_small_circles_ring,
    draw_patch_ring,
)


def draw_outer_orange_yellow_patch_ring(pen: turtle.Turtle) -> None:
    draw_patch_ring(pen, 860, 23, 160, ["#f88605", "#ffea00"])


def draw_outer_red_orange_triangle_band(pen: turtle.Turtle) -> None:
    draw_circle(pen, radius=850, bg_color="#6a040f")
    draw_nested_circle_ring(
        pen,
        big_radius=835,
        small_radius=164,
        count=12,
        colors=["#9d0208", "#d00000", "#6a040f"],
        start_angle=15,
    )

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    triangle_patterns = [
        (830, "#DC2F02"),
        (798, "#E85D04"),
        (766, "#FAA307"),
        (734, "#FFBA08"),
        (702, "#fff8dc"),
    ]

    for length, color in triangle_patterns:
        draw_repeating_triangle_pattern(pen, length, color, 12)
        pen.right(3)

    draw_paired_small_circles_ring(
        pen,
        big_radius=820,
        small_radius=12,
        pair_count=12,
        colors=["#00b4d8", "#4361ee", "#7209b7"],
        pair_gap_degrees=8,
        start_angle=0,
    )


def draw_outer_bright_green_triangle_ring(pen: turtle.Turtle) -> None:
    draw_radial_triangle_ring(pen, 36, 650, 700, 4.8, "#008000", -85)


def draw_outer_dark_green_triangle_ring(pen: turtle.Turtle) -> None:
    draw_radial_triangle_ring(pen, 36, 650, 700, 4.8, "#001A00", -90)


def draw_inner_red_patch_ring(pen: turtle.Turtle) -> None:
    draw_patch_ring(pen, 640, 17, 144, ["#A30000", "#D10000"])
