import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color('white')
        self.speed(11)
        self.goto(random.randint(-300, 300),random.randint(-300, 300))