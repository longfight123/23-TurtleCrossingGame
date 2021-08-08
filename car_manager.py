from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    A class used to manage the cars on the
    screen.

    ...

    Attributes
    ----------
    car_countdown: int
        the count down until adding the next car
    car_list: list
        a list that contains all the
        turtle objects on the screen
    level: int
        the current level in the game

    Methods
    -------
    create_car()
        adds a new turtle object to the
        car_list attribute and resets the countdown
    move_cars()
        move all cars forward
    increase_speed()
        increases the level of the game by 1
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_countdown = 6
        self.car_list = []
        self.level = 0

    def create_car(self):
        """adds a new turtle object to the
        car_list attribute and resets the countdown
        """
        if self.car_countdown == 1:
            new_car = Turtle('square')
            new_car.speed('fastest')
            new_car.penup()
            new_car.setheading(to_angle=180)
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(a=-250, b=250))
            self.car_list.append(new_car)
            self.car_countdown = 6
        else:
            self.car_countdown -= 1

    def move_cars(self):
        """move all cars forward
        """
        for each_car in self.car_list:
            new_x = each_car.xcor() - STARTING_MOVE_DISTANCE - (self.level * MOVE_INCREMENT)
            each_car.goto(x=new_x, y=each_car.ycor())

    def increase_speed(self):
        """increases the level of the game by 1
        """
        self.level += 1

