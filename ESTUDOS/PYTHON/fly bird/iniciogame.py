import pygame
import sys
import random

class Bird:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.gravity = 0.5
        self.lift = -12
        self.velocity = 0

    def show(self):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, 50, 50))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y > 550:
            self.y = 550
            self.velocity = 0

        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def up(self):
        self.velocity += self.lift

class Obstacle:
    def __init__(self):
        self.x = 800
        self.y = random.randint(200, 400)
        self.width = 50
        self.height = random.randint(100, 300)
        self.speed = 5

    def show(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.y))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y + self.height, self.width, 600 - self.y - self.height))

    def update(self):
        self.x -= self.speed

    def offscreen(self):
        return self.x < -self.width
    
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fly Bird Game")

bird = Bird()
obstacles = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.up()

    screen.fill((0, 0, 0))

    bird.show()
    bird.update()

    if random.randint(0, 100) < 1:
        obstacles.append(Obstacle())

    for obstacle in obstacles:
        obstacle.show()
        obstacle.update()

        if obstacle.offscreen():
            obstacles.remove(obstacle)

    pygame.display.update()
    clock.tick(60)