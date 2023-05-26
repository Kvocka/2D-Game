import pygame

pygame.init()
pygame.mixer.init()

collide_sound = "death.mp3"
collide = pygame.mixer.Sound(collide_sound)
channel3 = pygame.mixer.Channel(0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_right = pygame.image.load("player_right.png")
        self.image_left = pygame.image.load("player_left.png")
        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.vx = 50
        self.vy = 50
        self.lives = 3
        self.score = 0

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self._handle_boundaries()

    def handle_input(self, key, pressed):
        if key == pygame.K_UP:
            self.vy = -5 if pressed else 0
        if key == pygame.K_DOWN:
            self.vy = 5 if pressed else 0
        if key == pygame.K_LEFT:
            self.vx = -5 if pressed else 0
            self.image = self.image_left
        if key == pygame.K_RIGHT:
            self.vx = 5 if pressed else 0
            self.image = self.image_right

    def _handle_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 640:
            self.rect.right = 640
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480

    def collisions(self, enemies, collectible):
        # Collisions with enemies
        enemy_collisions = pygame.sprite.spritecollide(self, enemies, False)
        if enemy_collisions:
            self.lives -= 1
            #collide.play()
        # Collisions with collectibles
        collectible_collision = pygame.sprite.collide_rect(self, collectible)
        if collectible_collision:
            self.score += 1