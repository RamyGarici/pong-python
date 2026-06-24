from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.bgpic("pong.gif")



screen.tracer(0)
paddle1=Paddle(1)
paddle2=Paddle(2)
ball=Ball()
scoreboard=ScoreBoard()

drawing=Turtle()
drawing.color("white")
drawing.hideturtle()





screen.listen()
screen.onkeypress(paddle1.go_up,"Up")
screen.onkeypress(paddle1.go_down,"Down")

screen.onkeypress(paddle2.go_up,"a")
screen.onkeypress(paddle2.go_down,"q")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()
    if ball.distance(paddle1)<=50 and ball.xcor()>=340 or ball.distance(paddle2)<=50 and ball.xcor()<=-340:
        ball.bounce_x()
        
    if ball.xcor()>=380:
        scoreboard.l_point()
        ball.reset()
    elif ball.xcor()<=-380:
        scoreboard.r_point()
        ball.reset()
    if scoreboard.l_score==7 or scoreboard.r_score==7:
        scoreboard.end()
        game_is_on=False

   





screen.exitonclick()