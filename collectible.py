import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("collectible.png")
        self.rect = self.image.get_rect()