
import pygame

from snake_game.color import Color
from snake_game.food import Food
from snake_game.snake import Snake


class SnakeGame:
    def __init__(self, display_width=800, display_height=600, caption="Sankey Game"):
        success, failure = pygame.init()
        if failure > 0:
            print("WARNING: something did not initialize.")
        self.display_width = display_width
        self.display_height = display_height
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption(caption)
        self.game_over = False
        self.game_close = False
        self.snake = Snake(init_x_pos=display_width/2, init_y_pos=display_height/2, color=Color.pink, speed=15)
        self.font = pygame.font.SysFont("newyorkitalic", 30)
        self.clock = pygame.time.Clock()
        self.food = Food(size=self.snake.size, x_max=self.display_width, y_max=self.display_height)
        self.score = self.snake.length_of_snake - 1
        self.high_score = 0

    def message(self, msg, selected_color):
        display_msg = self.font.render(msg, True, selected_color)
        self.display.blit(display_msg, [self.display_width/2, self.display_height/2])

    def draw_score(self):
        score_msg = self.font.render(f"Score: {self.score} // High Score: {self.high_score}", True, Color.blue)
        self.display.blit(score_msg, [0,0])

    def draw_snake(self):
        for segment in self.snake.segments:
            pygame.draw.rect(self.display, self.snake.color, [segment[0], segment[1], self.snake.size, self.snake.size])

    def draw_food(self):
        pygame.draw.rect(self.display, Color.red, [self.food.x1, self.food.y1, self.food.size, self.food.size])

    def _get_events(self):
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if not self.game_close:
                    if event.key == pygame.K_LEFT:
                        self.snake.snake_left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.snake_right()
                    elif event.key == pygame.K_UP:
                        self.snake.snake_up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.snake_down()
                    return
                if event.key == pygame.K_y:
                    self.game_over = False
                    self.game_close = False
                    self.snake.initialize_snake(self.display_width/2, self.display_height/2)
                    break
                if event.key == pygame.K_n:
                    self.game_over = True
                    self.game_close = False
                    break

    def play_game(self):
        while not self.game_over:
            while self.game_close:
                self.display.fill(Color.blue)
                self.message("YOU LOST!!!", Color.white)
                self.score = self.snake.length_of_snake - 1
                self.draw_score()
                pygame.display.update()
                self._get_events()

            self._get_events()

            if self.snake.x1 >= self.display_width or self.snake.x1 < 0 or self.snake.y1 >= self.display_height or self.snake.y1 < 0:
                self.game_close = True

            self.snake.move_snake_head()

            self.display.fill(Color.white)

            self.draw_food()
            self.draw_snake()

            self.snake.add_snake_length()
            self.snake.check_snake_length()

            for segment in self.snake.segments[:-1]:
                if segment == self.snake.snake_head:
                    self.game_close = True

            self.draw_snake()

            self.score = self.snake.length_of_snake - 1
            if self.score > self.high_score:
                self.high_score = self.score
            self.draw_score()

            pygame.display.update()

            if self.snake.x1 == self.food.x1 and self.snake.y1 == self.food.y1:
                print("YUMMY!")
                self.food.food_placement()
                self.snake.length_of_snake += 1
                self.snake.speed += 1

            self.clock.tick(self.snake.speed)

        pygame.display.update()
        pygame.quit()






