from turtle import Turtle

#Constants
STARTING_POINT = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def create_snake(self):
        #Create default 3 squares
        for pos in STARTING_POINT:
            self.add_segment(pos)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    #Snake control logic
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    #Snake growing method
    def grow(self):
        #select last segment
        last_segment = self.segments[-1].position()
        self.add_segment(last_segment)
