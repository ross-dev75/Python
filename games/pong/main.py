from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
sleep_timer = ball.move_speed

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

out_of_bounds_limit = 2
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.wall_bounce()

    # Detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        # needs to bounce
        ball.paddle_bounce()
        ball.speed_up()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        # needs to bounce
        ball.paddle_bounce()
        ball.speed_up()

    # Detect out of bounds, update score for opposite player
    if ball.xcor() > 390:
        if out_of_bounds_limit > 0:
            ball.reset_position()
            out_of_bounds_limit -= 1
            scoreboard.update_l_score()
        else:
            game_on = False
            scoreboard.declare_winner()

    if ball.xcor() < -390:
        if out_of_bounds_limit > 0:
            ball.reset_position()
            out_of_bounds_limit -= 1
            scoreboard.update_r_score()
        else:
            game_on = False
            scoreboard.declare_winner()

screen.exitonclick()