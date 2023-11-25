import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Definição de constantes
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_SIZE = 20
FPS = 10

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid_size = GRID_SIZE
        self.snake_size = SNAKE_SIZE
        self.fps = FPS

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = RIGHT
        self.food = self.generate_food()

        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.level = 1

    def generate_food(self):
        while True:
            food = (random.randint(0, (self.width - self.grid_size) // self.grid_size) * self.grid_size,
                    random.randint(0, (self.height - self.grid_size) // self.grid_size) * self.grid_size)

            if food not in self.snake:
                return food

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            self.move()
            self.check_collision()
            self.check_food()

            # Desenhar na tela
            self.screen.fill(BLACK)
            self.draw_snake()
            self.draw_food()
            self.draw_score()

            pygame.display.flip()
            self.clock.tick(self.fps)

    def move(self):
        x, y = self.snake[0]
        x += self.direction[0] * self.grid_size
        y += self.direction[1] * self.grid_size

        # Verificar se a cobra atingiu as bordas da tela
        x = x % self.width
        y = y % self.height

        # Adicionar nova cabeça à cobra
        self.snake.insert(0, (x, y))

        # Remover última parte da cobra
        if self.snake[0] == self.food:
            self.score += 1
            if self.score % 5 == 0:
                self.level += 1
                self.fps += 2
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def check_collision(self):
        if self.snake[0] in self.snake[1:]:
            self.game_over()

    def check_food(self):
        if self.snake[0] == self.food:
            self.food = self.generate_food()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, WHITE, (segment[0], segment[1], self.snake_size, self.snake_size))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], self.snake_size, self.snake_size))

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, (10, 10))


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
