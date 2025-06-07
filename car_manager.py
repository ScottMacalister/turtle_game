from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.goto(x=320, y=random.randint(-250, 250))
            self.all_cars.append(car)

    def move_forward(self):
        for _ in self.all_cars:
            _.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT