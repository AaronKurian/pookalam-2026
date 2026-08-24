from __future__ import annotations

import turtle

from geometry import blend_hex_color
from primitives import draw_annular_sector


def draw_radial_color_pattern(pen: turtle.Turtle) -> None:
    palette = ["#fff8dc", "#fcbf49", "#f77f00", "#d62828", "#9d0208"]
    rings = [(78, 108), (108, 139), (139, 170), (170, 200)]
    divisions = 24

    for ring_index, (inner_radius, outer_radius) in enumerate(rings):
        for i in range(divisions):
            color = palette[(i + ring_index) % len(palette)]
            start = i * 360 / divisions
            end = (i + 1) * 360 / divisions
            draw_annular_sector(pen, inner_radius, outer_radius, start, end, color)


def draw_center_cyan_mint_sector_pattern(pen: turtle.Turtle) -> None:
    radii = list(range(78, 7, -5))
    center_colors = [
        (
            radius,
            [
                blend_hex_color("#91ffff", "#ecfff0", index / (len(radii) - 1)),
                blend_hex_color("#08a4a7", "#a4f5b0", index / (len(radii) - 1)),
            ],
        )
        for index, radius in enumerate(radii)
    ]

    for radius, colors in center_colors:
        for i in range(8):
            start = 90 - (i + 1) * 45
            end = 90 - i * 45
            draw_annular_sector(pen, 0, radius, start, end, colors[i % len(colors)], steps=12)
