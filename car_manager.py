COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_manager_i = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
                car=Turtle("square")
                car.color(random.choice(COLORS))
                car.penup()
                car.shapesize(stretch_len=2,stretch_wid= 1 )
                car.goto(250,random.randint(-250,250))
                car.setheading(180)
                self.car_manager_i.append(car)
    def movement(self):
        for car in self.car_manager_i:
            car.forward(self.car_speed)
    def increase_speed(self):
            self.car_speed+= MOVE_INCREMENT


