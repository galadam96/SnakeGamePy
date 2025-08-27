from turtle import Turtle

STARTING_COORD = (0,260)
GAME_OVER_COORD = (0,0)
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(STARTING_COORD)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))


    def refresh_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(GAME_OVER_COORD)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)