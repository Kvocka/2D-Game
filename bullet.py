import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, rotation) -> None:
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

