import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.title("Breakout Game")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with upper wall
    if ball.ycor() > 320:
        ball.bounce_y()

    # Detect collision with side walls
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with lower wall
    if ball.ycor() < -320:
        ball.reset_position()
        scoreboard.next_turn()

    # Detect collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with bricks
    if 155 < ball.ycor() < 165:
        for brick in bricks.yellow_bricks2:
            if ball.distance(brick) < 50:
                bricks.remove_yellow_brick2(brick)
                ball.bounce_y()
                scoreboard.inc_score(1)

    elif 175 < ball.ycor() < 185:
        for brick in bricks.yellow_bricks1:
            if ball.distance(brick) < 45:
                bricks.remove_yellow_brick1(brick)
                ball.bounce_y()
                scoreboard.inc_score(1)

    elif 195 < ball.ycor() < 205:
        for brick in bricks.green_bricks2:
            if ball.distance(brick) < 45:
                bricks.remove_green_brick2(brick)
                ball.bounce_y()
                scoreboard.inc_score(3)

    elif 215 < ball.ycor() < 225:
        for brick in bricks.green_bricks1:
            if ball.distance(brick) < 45:
                bricks.remove_green_brick1(brick)
                ball.bounce_y()
                scoreboard.inc_score(3)

    elif 235 < ball.ycor() < 245:
        for brick in bricks.orange_bricks2:
            if ball.distance(brick) < 45:
                bricks.remove_orange_brick2(brick)
                ball.bounce_y()
                scoreboard.inc_score(5)

    elif 255 < ball.ycor() < 265:
        for brick in bricks.orange_bricks1:
            if ball.distance(brick) < 45:
                bricks.remove_orange_brick1(brick)
                ball.bounce_y()
                scoreboard.inc_score(5)

    elif 275 < ball.ycor() < 285:
        for brick in bricks.red_bricks2:
            if ball.distance(brick) < 45:
                bricks.remove_red_brick2(brick)
                ball.bounce_y()
                scoreboard.inc_score(7)

    elif 295 < ball.ycor() < 305:
        for brick in bricks.red_bricks1:
            if ball.distance(brick) < 45:
                bricks.remove_red_brick1(brick)
                ball.bounce_y()
                scoreboard.inc_score(7)


turtle.mainloop()