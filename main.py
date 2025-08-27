from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#CONSTANTS
SCREEN_POS_X = 290
SCREEN_POS_Y = 290
SCREEN_NEG_X = -290
SCREEN_NEG_Y = -290

#End of DEFs
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Turn off animation
# Creating objects from Classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()
#Keyboard controls
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

#Game logic
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.update_position()
        snake.grow()
        scoreboard.increase_score()
        scoreboard.refresh_score()

    #Detect collision with wall
    if (snake.head.ycor() >= SCREEN_POS_Y or snake.head.ycor() <= SCREEN_NEG_Y or
        snake.head.xcor() >= SCREEN_POS_X or snake.head.xcor() <= SCREEN_NEG_X):
        # game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset_snake()

    #Detect collision with tail

    for segments in snake.segments[1:]: #Slice select all segments, except 1st (head)
        if snake.head.distance(segments) < 10:
            # game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset_score()


screen.exitonclick()
