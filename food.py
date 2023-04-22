from turtle import Turtle
import random


COLOR = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white"]


# random = random.choice(COLOR)
class Food(Turtle):
    """ return food position. 

    Args:
        Turtle (shape): _description_ food size=circle.
        Turtle (shapesize): _description_ food shape "reshape" hear.
        Turtle (color): _description_ food color blue.
        Turtle (shape): _description_ food size=circle.
     
    """
    
    def __init__(self):
        """ Use supper class to turtle module and use Turtle class.
        """
        super().__init__() 
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()
    
    def random_food_color(self):
        """ Return random color"""
        random_food_color = random.randint(0,7)
        return random_food_color
        
    def refresh(self):
        """From food class. random generate two number use random number for food position.
        use from turtle module use goto function.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(x=random_x, y=random_y)
        self.color(COLOR[self.random_food_color()])
        
