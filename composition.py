from __future__ import annotations

import turtle

from center import draw_center_cyan_mint_sector_pattern, draw_radial_color_pattern
from diyas import draw_diyas_around_pookalam
from geometry import leaf_points, radial_points, scaled_width
from images import place_maveli_image, place_wish_image
from outer_layers import (
    draw_inner_red_patch_ring,
    draw_outer_bright_green_triangle_ring,
    draw_outer_dark_green_triangle_ring,
    draw_outer_orange_yellow_patch_ring,
    draw_outer_red_orange_triangle_band,
)
from pentagons import draw_pentagon_triangle_pattern
from petals import draw_violet_blue_petal_band
from circles import draw_circle
from rings import draw_paired_small_circles_ring


def draw_white_triangle_blue_dot_pairs(pen: turtle.Turtle) -> None:
    draw_paired_small_circles_ring(
        pen,
        big_radius=600,
        small_radius=12,
        pair_count=8,
        colors=["#00b4d8", "#4361ee", "#7209b7"],
        pair_gap_degrees=20,
        start_angle=-67.5,
    )


def draw_leaf_outline_ring(pen: turtle.Turtle) -> None:
    base_leaf = leaf_points()
    colors = ["#ffd400", "#fff8dc"]
    pen.pensize(scaled_width(39))

    for i in range(8):
        points = radial_points(base_leaf, i * 45 - 90, 160)
        pen.color(colors[i % 2])
        pen.penup()
        pen.goto(points[0])
        pen.pendown()
        for point in points[1:]:
            pen.goto(point)
        pen.goto(points[0])


def draw_pookalam_layers(pen: turtle.Turtle) -> None:
    draw_outer_orange_yellow_patch_ring(pen)
    draw_outer_red_orange_triangle_band(pen)
    draw_outer_bright_green_triangle_ring(pen)
    draw_outer_dark_green_triangle_ring(pen)
    draw_circle(pen, radius=650, bg_color="#1b5e20")
    draw_inner_red_patch_ring(pen)
    draw_pentagon_triangle_pattern(pen)
    draw_white_triangle_blue_dot_pairs(pen)
    draw_violet_blue_petal_band(pen)
    draw_circle(pen, radius=335, bg_color="#6a040f")
    draw_leaf_outline_ring(pen)
    draw_circle(pen, radius=230, bg_color="#1b5e20")
    draw_radial_color_pattern(pen)
    draw_center_cyan_mint_sector_pattern(pen)
    place_maveli_image()
    draw_diyas_around_pookalam(pen)


def draw_pookalam() -> None:
    turtle.tracer(40, 0)
    turtle.bgcolor("#fffdf4")

    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    draw_pookalam_layers(pen)
    place_wish_image()
    turtle.update()
