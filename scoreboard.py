from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    A class used to represent a Scoreboard

    ...

    Attributes
    ----------
    current_level: int
        the current level in the game

    Methods
    -------
    refresh_score()
        updates the current level on the screen
    game_over()
        updates the screen to say game over
    """
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.goto(x=-275, y=250)
        self.current_level = 0
        self.refresh_score()

    def refresh_score(self):
        """updates the current level on the screen
        """
        self.clear()
        self.current_level += 1
        self.write(arg=f'Current level: {self.current_level}', font=FONT)

    def game_over(self):
        """updates the screen to say game over
        """
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER.', align='center', font=FONT)