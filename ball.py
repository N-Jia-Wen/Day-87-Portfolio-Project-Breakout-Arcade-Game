from turtle import Turtle
from random import choice, randint

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
random_x = [-8, -5, -2, 2, 5, 8]
random_y = [-8, -5]


class Ball(Turtle):
    def __init__(self):
        # Ball can start moving either right or left, but will always go downwards
        self.x_speed = 1
        self.x_move = choice(random_x) * self.x_speed
        self.y_move = choice(random_y)

        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.75)
        self.penup()
        self.goto(0, -50)

    def ball_move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def paddle_bounce(self, new_x_move):
        self.x_move = new_x_move
        self.y_move *= -1

    def vertical_wall_bounce(self):
        self.x_move *= -1

    def horizontal_wall_bounce(self):
        self.y_move *= -1

    def speed_up(self):
        self.y_move *= 1.2
        self.x_speed *= 1.2

    def check_ball_collision(self, paddle, start_pos, screen_width, screen_height):
        # For paddle collision. Accounts for paddle thickness.
        if start_pos[1] <= self.ycor() < start_pos[1] + 20:

            # Ball trajectory changes randomly when colliding with paddle:
            if self.distance(paddle) < 50:
                new_x_move = choice(random_x) * self.x_speed
                self.paddle_bounce(new_x_move)

        # For wall collision. The -12 accounts for the fact that ball's coordinates takes the centre of the ball:
        if self.xcor() > screen_width / 2 - 12 or self.xcor() < -(screen_width / 2 - 12):
            self.vertical_wall_bounce()
        if self.ycor() > screen_height / 2 - 12:
            self.horizontal_wall_bounce()


