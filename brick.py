from turtle import Turtle

RIGHT = 0
BRICK_WIDTH = 20 * 3.5
BRICK_HEIGHT = 20 * 1.6


class Brick(Turtle):
    def __init__(self, colour, x, y):
        super().__init__()
        self.create_brick(colour, x, y)
        self.top_left = (self.xcor() - BRICK_WIDTH/2, self.ycor() + BRICK_HEIGHT/2)
        self.top_right = (self.xcor() + BRICK_WIDTH/2, self.ycor() + BRICK_HEIGHT/2)
        self.bottom_left = (self.xcor() - BRICK_WIDTH/2, self.ycor() - BRICK_HEIGHT/2)
        self.bottom_right = (self.xcor() + BRICK_WIDTH/2, self.ycor() - BRICK_HEIGHT/2)

    def create_brick(self, colour, x, y):
        self.shape("square")
        self.color(colour)
        self.setheading(RIGHT)
        self.shapesize(stretch_wid=1.6, stretch_len=3.5)
        self.penup()
        self.goto(x, y)
