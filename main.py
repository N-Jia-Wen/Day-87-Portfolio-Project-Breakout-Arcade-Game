from turtle import Screen
from player import Player
from bricks_manager import BricksManager
from ball import Ball
from scoreboard import ScoreBoard
import time

game_running = True
difficulty = "Easy"
PLAYER_START_POS = (0, -250)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Setting up screen:
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Breakout Arcade Game")
screen.tracer(0)

player = Player(PLAYER_START_POS)

# Player movement:
screen.listen()
screen.onkeypress(fun=player.move_right, key="Right")
screen.onkeypress(fun=player.move_left, key="Left")

bricks_manager = BricksManager()
ball = Ball()
scoreboard = ScoreBoard()


while game_running is True:
    screen.update()
    time.sleep(0.03)
    ball.ball_move()
    ball.check_ball_collision(player, PLAYER_START_POS, SCREEN_WIDTH, SCREEN_HEIGHT)
    bricks_manager.check_brick_collision(ball)
    scoreboard.increment_score(bricks_manager)

    if scoreboard.score > 10 and difficulty == "Easy":
        difficulty = "Medium"
        ball.speed_up()
    elif scoreboard.score > 20 and difficulty == "Medium":
        difficulty = "Hard"
        ball.speed_up()
    elif scoreboard.score > 30 and difficulty == "Hard":
        difficulty = "Very Hard"
        ball.speed_up()
    elif scoreboard.score > 40 and difficulty == "Very Hard":
        difficulty = "Maximum"
        ball.speed_up()

    if ball.ycor() < - 400 or bricks_manager.bricks_list == []:
        game_running = False
        scoreboard.final_score()


screen.exitonclick()
