from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Helvetica", 14, "normal"))

    def write_score(self, score):
        self.write(f"Score : {score}", False, align="center", font=("Helvetica", 14, "normal"))
