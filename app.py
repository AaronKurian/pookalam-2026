import turtle

from composition import draw_pookalam
from config import CANVAS_SIZE


def main() -> None:
    screen = turtle.Screen()
    screen.setup(width=CANVAS_SIZE, height=CANVAS_SIZE)
    screen.title("Code-A-Pookalam 2026")
    screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
    draw_pookalam()
    screen.exitonclick()
