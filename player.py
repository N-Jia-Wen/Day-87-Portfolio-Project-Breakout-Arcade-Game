from turtle import Turtle
from random import randint

RIGHT = 0
LEFT = 180


# Taken from Day 22 - Creating Pong:
class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_player(position)

    def create_player(self, position):
        self.shape("square")
        self.color("blue")
        self.setheading(RIGHT)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_right(self):
        self.forward(50)

    def move_left(self):
        self.backward(50)
