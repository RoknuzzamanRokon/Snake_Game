from turtle import Turtle


# Here is constant.
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    """ Call super class for Turtle class. when call supper class then class object
    call directly. here using goto,color,hideturtle etc. method from Turtle class."""
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as score:
            self.high_score = int(score.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Here use Turtle class "write" function.hera show update scoreboard. 
        """
        self.clear()
        self.write(f"Your score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as score_tracker:
                score_tracker.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_scoreboard(self):
        """ Increase score and using "clear" method from Turtle class. and call update_scoreboard.
        """
        self.score += 1        
        self.clear()
        self.update_scoreboard()

    # def game_over_massage(self):
    #     """ Show game over massage."""
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=('Courier', 50, 'normal'))
    #     self.goto(0, -30)
    #     self.write(f"Your score: {self.score}", align=ALIGNMENT, font=FONT)

