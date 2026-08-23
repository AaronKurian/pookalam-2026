from __future__ import annotations

import turtle

from geometry import scaled, scaled_width


def draw_circle(
    pen: turtle.Turtle,
    radius: float,
    bg_color: str | None,
    border_color: str | None = None,
    thickness: int = 1,
) -> None:
    radius = scaled(radius)
    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    pen.pensize(scaled_width(thickness))
    pen.color(border_color or bg_color)
    pen.pendown()
    if bg_color is not None:
        pen.fillcolor(bg_color)
        pen.begin_fill()
    pen.circle(radius)
    if bg_color is not None:
        pen.end_fill()
    pen.penup()


def draw_circle_at(
    pen: turtle.Turtle,
    center: tuple[float, float],
    radius: float,
    bg_color: str,
    border_color: str | None = None,
    thickness: int = 1,
) -> None:
    radius = scaled(radius)
    pen.penup()
    pen.goto(center[0], center[1] - radius)
    pen.setheading(0)
    pen.pensize(scaled_width(thickness))
    pen.color(border_color or bg_color, bg_color)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()


def draw_nested_circle_at(
    pen: turtle.Turtle,
    center: tuple[float, float],
    radius: float,
    colors: list[str],
) -> None:
    for index, color in enumerate(colors):
        layer_radius = scaled(radius * (len(colors) - index) / len(colors))
        pen.penup()
        pen.goto(center[0], center[1] - layer_radius)
        pen.setheading(0)
        pen.color(color, color)
        pen.pendown()
        pen.begin_fill()
        pen.circle(layer_radius)
        pen.end_fill()

    pen.penup()
