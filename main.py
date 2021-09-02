from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0, 0)

screen.update()
screen.listen()

scoreboard = Scoreboard()

snake = Snake()
food = Food()

screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect eating food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.score_up()
        snake.grow()

    # Detect Wall
    if \
            snake.head.xcor() > 280 \
                    or\
            snake.head.xcor() < -280\
                    or\
            snake.head.ycor() > 280\
                    or\
            snake.head.ycor() < -280:
        game_is_on = False

#     detect self collision
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()
