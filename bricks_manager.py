from brick import Brick

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICKS_PER_ROW = 10
NO_OF_ROWS = 8
COLOURS = ["green", "green", "yellow", "yellow", "orange", "orange", "red", "red"]


class BricksManager:

    def __init__(self):
        self.bricks_list = []
        self.bricks_destroyed = []
        self.generate_bricks()

    def generate_bricks(self):
        # Loading bricks:
        brick_height = SCREEN_HEIGHT / 2 / NO_OF_ROWS
        # The -5 is added as a buffer so that bricks are not displayed outside the window
        brick_width = SCREEN_WIDTH / BRICKS_PER_ROW - 5

        for num in range(len(COLOURS)):
            colour = COLOURS[num]
            y = num * brick_height
            for nth_brick in range(1, BRICKS_PER_ROW + 1):
                # Using arithmetic sequence formula (and trial and error to render bricks properly):
                x = -340 + (nth_brick - 1) * brick_width
                brick = Brick(colour, x, y)
                self.bricks_list.append(brick)

    def check_brick_collision(self, ball):
        for brick in self.bricks_list:
            if ball.distance(brick) <= 40:

                if brick.top_left[0] <= ball.xcor() <= brick.top_right[0]:
                    # Ball collided with the top or bottom side of the brick
                    ball.y_move *= -1
                elif brick.bottom_left[1] <= ball.ycor() <= brick.top_left[1]:
                    # Ball collided with the left or right side of the brick
                    ball.x_move *= -1

                # Remove the brick from the list and destroy it
                self.bricks_list.remove(brick)
                self.bricks_destroyed.append(brick)
                brick.clear()
                brick.hideturtle()
                break
