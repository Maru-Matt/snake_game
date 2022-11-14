from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(len(STARTING_POSITIONS)):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(STARTING_POSITIONS[i])
            self.segments.append(new_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def add_segment(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        self.segments.append(new_turtle)

    def collide_with_tail(self):
        for i in range(1, len(self.segments)):
            if self.head.distance(self.segments[i]) < 10:
                return True

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
