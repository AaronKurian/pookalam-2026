from __future__ import annotations

import os
import turtle

from PIL import Image, ImageTk

from config import DESIGN_SCALE, MAVELI_IMAGE, WISH_IMAGE


_IMAGE_REFS: list[ImageTk.PhotoImage] = []


def place_image(image_path: os.PathLike[str] | str, center: tuple[float, float], max_size: tuple[float, float]) -> None:
    image = Image.open(image_path).convert("RGBA")
    image.thumbnail((round(max_size[0]), round(max_size[1])), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    _IMAGE_REFS.append(photo)
    turtle.getcanvas().create_image(center[0], center[1], image=photo)


def place_maveli_image() -> None:
    place_image(MAVELI_IMAGE, (0, 0), (130 * DESIGN_SCALE, 146 * DESIGN_SCALE))


def place_wish_image() -> None:
    place_image(WISH_IMAGE, (-550, -520), (300, 300))
