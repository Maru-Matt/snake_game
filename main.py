import time
from food import Food
from snake import Snake
from turtle import Screen
from score_board import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(my_snake.move_up, "Up")
screen.onkey(my_snake.move_down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision of snake with food
    if my_snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        my_snake.add_segment()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    if my_snake.collide_with_tail():
        game_is_on = False
        score.game_over()

screen.exitonclick()
