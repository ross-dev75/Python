from turtle import Turtle, Screen
import time



class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1

    def speed_up(self):
        self.move_speed *= 0.9

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def update_r_score(self):
        self.r_score += 1
        self.refresh()

    def update_l_score(self):
        self.l_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 24, "normal"))

    def declare_winner(self):
        self.goto(0, 0)
        if self.r_score == self.l_score:
            self.write("GAME OVER. TIE!", align="center", font=("Courier", 24, "normal"))
        elif self.r_score > self.l_score:
            self.write("GAME OVER.\nRIGHT WINS !", align="center", font=("Courier", 24, "normal"))
        else:
            self.write("GAME OVER.\nLEFT WINS !", align="center", font=("Courier", 24, "normal"))

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