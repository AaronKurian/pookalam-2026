from __future__ import annotations

import math
import turtle

from geometry import scaled
from patterns import draw_repeating_triangle_pattern
from circles import draw_circle
from primitives import draw_polygon


def draw_scaled_triangle_pattern(
    pen: turtle.Turtle,
    length: float,
    color: str,
    repeat_count: int,
    height_scale: float,
) -> None:
    pen.color(color)
    base = scaled(length / math.tan(math.pi / 3.6))
    side = scaled(length / math.sin(math.pi / 3.6))

    def point_from(origin: tuple[float, float], heading_deg: float, distance: float) -> tuple[float, float]:
        angle = math.radians(heading_deg)
        return origin[0] + distance * math.cos(angle), origin[1] + distance * math.sin(angle)

    def compress_point(
        point: tuple[float, float],
        base_start: tuple[float, float],
        base_end: tuple[float, float],
    ) -> tuple[float, float]:
        mid = ((base_start[0] + base_end[0]) / 2, (base_start[1] + base_end[1]) / 2)
        return (
            mid[0] + (point[0] - mid[0]) * height_scale,
            mid[1] + (point[1] - mid[1]) * height_scale,
        )

    for _ in range(repeat_count):
        heading = pen.heading()
        p0 = pen.position()
        p1 = point_from(p0, heading, base)
        p2 = point_from(p1, heading + 130, side)
        p3 = point_from(p2, heading + 230, side)
        draw_polygon(pen, [p0, p1, compress_point(p2, p0, p1), compress_point(p3, p0, p1)], fill=color)
        pen.goto(p0)
        pen.setheading(heading + 360 / repeat_count)

    pen.left(5)
    pen.penup()


def draw_violet_blue_petal_band(pen: turtle.Turtle) -> None:
    draw_circle(pen, radius=500, bg_color="#fff8dc")
    draw_circle(pen, radius=506, bg_color=None, border_color="#9acd32", thickness=14)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    draw_repeating_triangle_pattern(pen, 470, "#7D82B8", 36)
    draw_repeating_triangle_pattern(pen, 430, "#613F75", 36)
    draw_repeating_triangle_pattern(pen, 390, "#03071e", 36)
    draw_repeating_triangle_pattern(pen, 350, "#000814", 36)


def draw_outer_violet_blue_petal_band(pen: turtle.Turtle) -> None:
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    inner_patterns = [
        (845, "#7D82B8", 36),
        (785, "#613F75", 36),
        (725, "#03071e", 36),
    ]

    for length, color, repeat_count in inner_patterns:
        draw_scaled_triangle_pattern(pen, length, color, repeat_count, height_scale=0.86)
