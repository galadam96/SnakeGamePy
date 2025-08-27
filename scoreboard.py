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
        self.highscore = 0
        self.score = 0
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.refresh_score()

    # def game_over(self):
    #     self.goto(GAME_OVER_COORD)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
