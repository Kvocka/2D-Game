import pygame
import random

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("enemy1.png")
        self.rect = self.image.get_rect()

        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("enemy2.png")
        self.rect = self.image.get_rect()

        self.vx = random.randint(-2, 2)
        self.vy = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy