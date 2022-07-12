import random


class Food:
    """
    x_max: display width
    y_max: display height
    """
    def __init__(self, size, x_max, y_max):
        self.size = size
        self.x_max = x_max
        self.y_max = y_max
        self.x1 = round(random.randrange(self.size, self.x_max - self.size)) // 10 * 10
        self.y1 = round(random.randrange(self.size, self.y_max - self.size)) // 10 * 10

    def food_placement(self):
        self.x1 = round(random.randrange(self.size, self.x_max - self.size)) // 10 * 10
        self.y1 = round(random.randrange(self.size, self.y_max - self.size)) // 10 * 10
