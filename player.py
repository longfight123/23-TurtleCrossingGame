from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    A class used to represent the player.

    ...

    Methods
    -------
    reset_position()
        resets the player to the starting
        position
    move_up()
        move the player up
    """
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.speed('fastest')
        self.setheading(to_angle=90)
        self.reset_position()

    def reset_position(self):
        """resets the player to the starting
        position
        """
        self.goto(STARTING_POSITION)

    def move_up(self):
        """move the player up
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=0, y=new_y)
