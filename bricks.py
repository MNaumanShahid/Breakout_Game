from turtle import Turtle


RED_POS1 = [(i, 300) for i in range(-455, 455, 100)]
RED_POS2 = [(i, 280) for i in range(-455, 455, 100)]
ORANGE_POS1 = [(i, 260) for i in range(-455, 455, 100)]
ORANGE_POS2 = [(i, 240) for i in range(-455, 455, 100)]
GREEN_POS1 = [(i, 220) for i in range(-455, 455, 100)]
GREEN_POS2 = [(i, 200) for i in range(-455, 455, 100)]
YELLOW_POS1 = [(i, 180) for i in range(-455, 455, 100)]
YELLOW_POS2 = [(i, 160) for i in range(-455, 455, 100)]


class Bricks:

    def __init__(self):
        self.red_bricks1 = []
        self.orange_bricks1 = []
        self.green_bricks1 = []
        self.yellow_bricks1 = []
        self.red_bricks2 = []
        self.orange_bricks2 = []
        self.green_bricks2 = []
        self.yellow_bricks2 = []
        self.create_wall()
        self.wall = []

    def create_wall(self):
        for pos in RED_POS1:
            red_brick = Turtle("square")
            red_brick.color("red")
            red_brick.penup()
            red_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            red_brick.goto(pos)
            self.red_bricks1.append(red_brick)
        for pos in RED_POS2:
            red_brick = Turtle("square")
            red_brick.color("red")
            red_brick.penup()
            red_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            red_brick.goto(pos)
            self.red_bricks2.append(red_brick)
        for pos in ORANGE_POS1:
            orange_brick = Turtle("square")
            orange_brick.color("orange")
            orange_brick.penup()
            orange_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            orange_brick.goto(pos)
            self.orange_bricks1.append(orange_brick)
        for pos in ORANGE_POS2:
            orange_brick = Turtle("square")
            orange_brick.color("orange")
            orange_brick.penup()
            orange_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            orange_brick.goto(pos)
            self.orange_bricks2.append(orange_brick)
        for pos in GREEN_POS1:
            green_brick = Turtle("square")
            green_brick.color("green")
            green_brick.penup()
            green_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            green_brick.goto(pos)
            self.green_bricks1.append(green_brick)
        for pos in GREEN_POS2:
            green_brick = Turtle("square")
            green_brick.color("green")
            green_brick.penup()
            green_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            green_brick.goto(pos)
            self.green_bricks2.append(green_brick)
        for pos in YELLOW_POS1:
            yellow_brick = Turtle("square")
            yellow_brick.color("yellow")
            yellow_brick.penup()
            yellow_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            yellow_brick.goto(pos)
            self.yellow_bricks1.append(yellow_brick)
        for pos in YELLOW_POS2:
            yellow_brick = Turtle("square")
            yellow_brick.color("yellow")
            yellow_brick.penup()
            yellow_brick.shapesize(stretch_len=4.5, stretch_wid=0.5)
            yellow_brick.goto(pos)
            self.yellow_bricks2.append(yellow_brick)

    def remove_red_brick1(self, brick):
        brick.hideturtle()
        self.red_bricks1.remove(brick)

    def remove_red_brick2(self, brick):
        brick.hideturtle()
        self.red_bricks2.remove(brick)

    def remove_orange_brick1(self, brick):
        brick.hideturtle()
        self.orange_bricks1.remove(brick)

    def remove_orange_brick2(self, brick):
        brick.hideturtle()
        self.orange_bricks2.remove(brick)

    def remove_green_brick1(self, brick):
        brick.hideturtle()
        self.green_bricks1.remove(brick)

    def remove_green_brick2(self, brick):
        brick.hideturtle()
        self.green_bricks2.remove(brick)

    def remove_yellow_brick1(self, brick):
        brick.hideturtle()
        self.yellow_bricks1.remove(brick)

    def remove_yellow_brick2(self, brick):
        brick.hideturtle()
        self.yellow_bricks2.remove(brick)
