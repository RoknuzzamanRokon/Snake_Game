# from turtle import Turtle, Screen


# turtle = Turtle()
# # Create the turtle instance and set its attributes
# button = Turtle(shape="square")
# button.color("white", "green")
# button.shapesize(stretch_wid=1, stretch_len=4)
# button.penup()
# button.goto(0, 0)

# # Register the button shape
# Screen().register_shape("button", ((-10,-10),(10,-10),(10,10),(-10,10)))

# # Use the button in your code
# button.shape("button")

# turtle.hideturtle()
# screen = Screen()
# turtle.write("Start Game", align="center", font=("Arial", 16, "bold"))



# screen.mainloop()


from turtle import Turtle,Screen

# Define the function to be called when the button is clicked
def start_game():
    print("Hello World!")

# Create the screen and turtle
screen = Screen()
turtle = Turtle()

# Create the button and register the function to be called when clicked
button = Turtle()
button.penup()
button.goto(0, -50)
button.write("Start Game", align="center", font=("Arial", 16, "bold"))
button.goto(0, -70)
button.pendown()
button.goto(0, -90)
button.goto(80, -90)
button.goto(80, -70)
button.goto(0, -70)

def on_button_click(x, y):
    if abs(x - button.xcor()) < 40 and abs(y - button.ycor()) < 20:
        start_game()

button.onclick(on_button_click)

# Keep the screen open
screen.mainloop()
