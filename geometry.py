from __future__ import annotations

import math

from config import DESIGN_SCALE


def scaled(value: float) -> float:
    return value * DESIGN_SCALE


def scaled_width(width: int) -> int:
    return max(1, round(width * DESIGN_SCALE))


def blend_hex_color(start: str, end: str, progress: float) -> str:
    start_rgb = tuple(int(start[i : i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end[i : i + 2], 16) for i in (1, 3, 5))
    rgb = tuple(round(a + (b - a) * progress) for a, b in zip(start_rgb, end_rgb))
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def polar_point(radius: float, angle_deg: float) -> tuple[float, float]:
    angle = math.radians(angle_deg)
    return scaled(radius * math.cos(angle)), scaled(radius * math.sin(angle))


def radial_points(points: list[tuple[float, float]], angle_deg: float, radius: float) -> list[tuple[float, float]]:
    angle = math.radians(angle_deg)
    radial = (math.cos(angle), math.sin(angle))
    tangent = (-math.sin(angle), math.cos(angle))

    return [
        (
            scaled(radius * radial[0] + x * tangent[0] - y * radial[0]),
            scaled(radius * radial[1] + x * tangent[1] - y * radial[1]),
        )
        for x, y in points
    ]


def leaf_points(
    height: float = 312,
    width: float = 280,
    steps: int = 140,
) -> list[tuple[float, float]]:
    left: list[tuple[float, float]] = []
    right: list[tuple[float, float]] = []

    for i in range(steps + 1):
        t = i / steps
        y = height / 2 - height * t
        bulb = math.sin(math.pi * t) ** 0.28
        lower_bulge = 0.24 + 2.35 * t
        top_taper = (1 - t) ** 1.18
        base_rounding = 1 - 0.5 * t + 0.34 * t * t
        x = width * bulb * lower_bulge * top_taper * base_rounding
        right.append((x, y))
        left.append((-x, y))

    return right + list(reversed(left))
