print("=== SNAKE MAIN IS RUNNING ===")

import time
from turtle import Screen


from snakemain import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake =  Snake()
food = Food()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect the collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()


    # detect collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()




















screen.exitonclick()



