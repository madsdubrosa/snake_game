

class Snake:
    def __init__(self, init_x_pos, init_y_pos, color, speed=15):
        self.initialize_snake(init_x_pos, init_y_pos, speed)
        self.size = 10
        self.color = color

    def initialize_snake(self, init_x_pos, init_y_pos, speed=15):
        self.x1 = init_x_pos
        self.y1 = init_y_pos
        self.x1_delta = 0
        self.y1_delta = 0
        self.segments = []
        self.length_of_snake = 1  # only a head in the initialization
        self.snake_head = [self.x1, self.y1]
        self.speed = speed

    def move_snake_head(self):
        self.x1 += self.x1_delta
        self.y1 += self.y1_delta

    def snake_left(self):
        self.x1_delta = -self.size
        self.y1_delta = 0

    def snake_right(self):
        self.x1_delta = self.size
        self.y1_delta = 0

    def snake_up(self):
        self.x1_delta = 0
        self.y1_delta = -self.size

    def snake_down(self):
        self.x1_delta = 0
        self.y1_delta = self.size

    def check_snake_length(self):
        if len(self.segments) > self.length_of_snake:
            del self.segments[0]

    def add_snake_length(self):
        self.snake_head = [self.x1, self.y1]
        self.segments.append(self.snake_head)
