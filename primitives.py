from __future__ import annotations

import turtle

from geometry import polar_point, scaled_width


def draw_polygon(
    pen: turtle.Turtle,
    points: list[tuple[float, float]],
    fill: str,
    outline: str | None = None,
    width: int = 1,
) -> None:
    pen.penup()
    pen.goto(points[0])
    pen.pensize(scaled_width(width))
    pen.color(outline or fill, fill)
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def draw_annular_sector(
    pen: turtle.Turtle,
    inner_radius: float,
    outer_radius: float,
    start_angle: float,
    end_angle: float,
    color: str,
    steps: int = 10,
) -> None:
    outer_points = [
        polar_point(outer_radius, start_angle + (end_angle - start_angle) * i / steps)
        for i in range(steps + 1)
    ]
    inner_points = [
        polar_point(inner_radius, end_angle - (end_angle - start_angle) * i / steps)
        for i in range(steps + 1)
    ]
    points = outer_points + inner_points

    pen.penup()
    pen.goto(points[0])
    pen.color(color, color)
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()
    pen.penup()

