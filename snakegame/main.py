from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score



screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()



snake.create_square()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    #detect collision with food
    if snake.serpiente[0].distance(food)< 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    if snake.serpiente[0].xcor()>290 or snake.serpiente[0].xcor()< -300 or snake.serpiente[0].ycor()>300 or snake.serpiente[0].ycor()<-290:
        score.reset()
        snake.reset()
      
     


    for segment in snake.serpiente[1:]:
        if snake.serpiente[0].distance(segment) < 10:
            score.reset()
            snake.reset()
          
           





    
        

   

screen.exitonclick()