from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(0, -300)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())