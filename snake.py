from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(pos)
            self.snake_segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            next_seg = self.snake_segments[seg_num - 1]
            self.snake_segments[seg_num].goto(next_seg.xcor(), next_seg.ycor())
        self.snake_segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
