from turtle import Turtle
import pyglet
from ctypes import windll

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# To fix blurry tkinter font. Taken from https://stackoverflow.com/questions/41315873/attempting-to-resolve-
# blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp/43046744#43046744
windll.shcore.SetProcessDpiAwareness(1)

# Rendering custom fonts. Taken from https://stackoverflow.com/questions/11993290/truly-custom-font-in-tkinter
pyglet.font.add_file('./fonts/arcadeclassic/ARCADECLASSIC.TTF')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(320, -290)
        self.write(arg=f"Score: {self.score}", align="center", font=("ArcadeClassic", 14, "normal"))

    def increment_score(self, bricks_manager):
        self.score = 0
        for brick in bricks_manager.bricks_destroyed:
            if brick.color()[0] == "green":
                self.score += 1
            elif brick.color()[0] == "yellow":
                self.score += 3
            elif brick.color()[0] == "orange":
                self.score += 5
            elif brick.color()[0] == "red":
                self.score += 7

            self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.goto(0, -100)
        self.write(arg=f"Final Score: {self.score}", align="center", font=("ArcadeClassic", 30, "normal"))