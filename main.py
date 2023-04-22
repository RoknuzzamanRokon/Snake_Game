from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time 


turtle = Turtle()
# Game screen layout.size,color and title here.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My snack game')
screen.tracer(0)

# Use Snake class.and create an object name snake.
snake = Snake()

# Use Food class.and create an object name food.
food_1 = Food()
food_2 = Food()
food_3 = Food()


turtle.hideturtle()
turtle.penup()
turtle.goto((-300, 265))
turtle.pendown()
turtle.pensize(3)
turtle.pencolor("red")
turtle.forward(600)

# Use Scoreboard class.and create an object name scoreboard.
scoreboard = Scoreboard()


# Using Turtle class from "listen" method.Create Up Down Left Right.
screen.listen()
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')

screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')


# Create a Boolean function.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food.
    if snake.head.distance(food_1) < 10:
        food_1.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()
    elif snake.head.distance(food_2) < 10:   
        food_2.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()
    elif snake.head.distance(food_3) < 10:   
        food_3.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()    
    
        #  Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 260 or snake.head.ycor() < -295:  
        # game_is_on = False
        # scoreboard.game_over_massage()

        scoreboard.reset()
        snake.reset()

        # Detect collision with tail.
    for i in snake.segment[1:]:
        if snake.head.distance(i) < 5:
            # game_is_on = False
            # scoreboard.game_over_massage()

            scoreboard.reset()
            snake.reset()
        
screen.exitonclick()