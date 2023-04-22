# from turtle import Screen, Turtle

# # Create the first screen and set its color
# screen1 = Screen()
# screen1.bgcolor("red")

# # Set up the first screen with desired attributes
# screen1.setup(width=800, height=800)
# screen1.title("First Screen")
# screen1.tracer(0)

# # Create the second screen and set its color
# screen2 = Screen()
# screen2.bgcolor("white")

# # Set up the second screen with desired attributes
# screen2.setup(width=600, height=600)
# screen2.title("Second Screen")
# screen2.tracer(0)

# # Create a turtle instance for each screen
# t1 = Turtle(screen=screen1)
# t2 = Turtle(screen=screen2)

# # Draw something on each screen using the turtle instances
# t1.color("yellow")
# t1.forward(100)

# t2.color("blue")
# t2.left(90)
# t2.forward(100)

# # Keep both screens open until manually closed
# screen1.done()
# screen2.done()






from turtle import Screen, Turtle

# Create the first screen and set its color
screen1 = Screen()
# screen1.bgcolor("red")

turtle = Turtle()

turtle.getscreen()
turtle.bgcolor('white')


# Set up the first screen with desired attributes
screen1.setup(width=800, height=800)
screen1.title("First Screen")
screen1.tracer(0)

# Create a turtle instance for the first screen
t1 = Turtle()
t1.setposition(0, 0)

# Create the second screen and set its color
screen2 = Screen()
screen2.bgcolor("white")

# Set up the second screen with desired attributes
screen2.setup(width=600, height=600)
screen2.title("Second Screen")
screen2.tracer(0)

# Create a turtle instance for the second screen
t2 = Turtle()
t2.setposition(0, 0)

# Exit on click
screen1.exitonclick()
screen2.exitonclick()



