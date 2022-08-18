import turtle

distance = 20
links = 3
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

# generating body
#     def create_snake(self):
#         for segment in range(0, links):
#             self.add_segment(segment)

    # def add_segment(self, segment):
    #     chain = turtle.Turtle(shape='square')
    #     chain.penup()
    #     chain.color('black')
    #     chain.goto(-20*segment, 0)
    #     self.segments.append(chain)
    #
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # default movement
    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(distance)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

# input movement


    def move_up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)
