from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.update_position()

    def update_position(self):
        rand_x = randint(-250, 250)
        rand_y = randint(-250, 250)
        self.goto(rand_x,rand_y)