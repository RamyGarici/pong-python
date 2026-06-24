from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 80, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 180)
        self.write(f"{self.l_score}   {self.r_score}", align=ALIGNEMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def end(self):
       
        self.clear()
        self.goto(0, 0)
        if self.l_score == 7:
            winner = "Left Player"
        else:
            winner = "Right Player"
        self.write(f"The winner is the {winner}.", align=ALIGNEMENT, font=("Courier", 30, "normal"))
