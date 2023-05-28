import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, reset_location = (0,0), screen_width = 640, screen_height = 480):
        super().__init__()
        self.dead_for = 0

        self.alive_image = pygame.image.load(image_file)
        self.image = self.alive_image
        self.reset_location = reset_location
        self.rect = self.image.get_rect()
        self.vx = speed
        self.vy = speed

        self.screen_width = screen_width
        self.screen_height = screen_height


    def update(self):
        if self.dead_for > 0:
            self.dead_for -= 1
            if self.dead_for == 0:
                self.vx = -self.vx
                self.vy = -self.vy
                self.image = self.alive_image
            return
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0:
            self.vx = abs(self.vx)
        
        if self.rect.right >= self.screen_width:
            self.vx = -abs(self.vx)
        
        if self.rect.top <= 0:
            self.vy = abs(self.vy)
        
        if self.rect.bottom >= self.screen_height:
            self.vy = -abs(self.vy)
        
      
    def reset(self):
        self.rect.left = self.reset_location[0]
        self.rect.top = self.reset_location[1]


    def collisions(self, bullets):
        # Collisions with bullets
        bullet_collisions = pygame.sprite.spritecollide(self, bullets, False)
        if bullet_collisions:
            self.dead_for = 60 * 2
            self.image = pygame.transform.grayscale(self.image)

