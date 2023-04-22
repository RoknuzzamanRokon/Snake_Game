from turtle import Turtle
import random

COLOR = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white"]


STARING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# Change snake body shape here.
SNAKE_SHAPE = ((-5, -5), (-5, 5), (5, 5), (5, -5))
t = Turtle()
t.screen.register_shape("snake", SNAKE_SHAPE)
t.shape("snake")


class Snake:
    """ Snake body,snake move and snake control button.
    """
    def __init__(self):
        """ Create an empty list name segment.call snake.sit snake head position.
        """
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """ Create snake.using constant for snake position.
        """
        for position in STARING_POSITION:
            self.add_segment(position)

    def random_snake_color(self):
        """Return random color"""
        
        random_color = random.randint(0, 7)
        return random_color

    def add_segment(self, position):
        """ Create an object form Turtle class. Using turtle color function for snake body.append all snake body.
            return snake body.
             """
        new_segment = Turtle("snake")
        
        new_segment.color(COLOR[self.random_snake_color()])
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self):
        for i in self.segment:
            i.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        """Move snake.Here using for lope for snake body position."""
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
            
