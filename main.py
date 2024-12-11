from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import score_board
import time 

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = score_board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#move the snake continuously until we change its direction
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
#detect the collision with the food
    if snake.head.distance(food)< 12:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
        
#Detect Collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -299 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

#Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <12:
            game_is_on = False
            scoreboard.game_over()
#if  head collides with any segment in the tail:
#trigger game over


screen.exitonclick()
 