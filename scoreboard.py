from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.turns = 2
        self.display = f"Score: {self.score}  Turns: {self.turns}"
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(0, 325)
        self.write(self.display, align="center", font=("Courier", 20, "normal"))
        self.goto(-500, 320)
        self.pendown()
        self.forward(1000)
        self.penup()

    def inc_score(self, score):
        self.score += score
        self.display = f"Score: {self.score}  Turns: {self.turns}"
        self.score_update()

    def next_turn(self):
        self.turns -= 1
        self.display = f"Score: {self.score}  Turns: {self.turns}"
        self.score_update()
