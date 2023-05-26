import pygame
import random
from player import Player
from enemy import Enemy1, Enemy2
from collectible import Collectible

# Initialize pygame
pygame.init()
pygame.mixer.init()

collect_sound = "collect.mp3"
collect = pygame.mixer.Sound(collect_sound)
channel2 = pygame.mixer.Channel(0)


collide_sound = "death.mp3"
collide = pygame.mixer.Sound(collide_sound)
channel3 = pygame.mixer.Channel(0)

# Screen settings
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("2D-Game")

# Background image
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))

# Create instances
player = Player()
enemy1 = Enemy1()
enemy2 = Enemy2()
collectible = Collectible()
score = 0

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites.add(player)
enemies.add(enemy1)
enemies.add(enemy2)
all_sprites.add(enemy1)
all_sprites.add(enemy2)
all_sprites.add(collectible)

# Game variables
running = True
clock = pygame.time.Clock()

# Main game loop
while running:
    # Update game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            player.handle_input(event.key, True)
        elif event.type == pygame.KEYUP:
            player.handle_input(event.key, False)

    all_sprites.update()
    screen.blit(background, (0, 0))

    player.collisions(enemies, collectible)

    if player.lives <= 0:
        print(":(")
        running = False
        # Display "Game Over" message and handle replay or exit

    if player.rect.colliderect(collectible.rect):
        score += 1
        print(score)
        if not channel2.get_busy():
            collect.play()
        collectible.rect.x = random.randint(0,580)
        collectible.rect.y = random.randint(0,400)

    if enemy1.rect.left <=0:
        enemy1.vx = 3    

    if enemy1.rect.right >=640:
        enemy1.vx = -3 

    if enemy1.rect.top <=0:
        enemy1.vy = 3   

    if enemy1.rect.bottom >=480:
        enemy1.vy = -3  

    if enemy2.rect.left <=0:
        enemy2.vx = 5    

    if enemy2.rect.right >=640:
        enemy2.vx = -5 

    if enemy2.rect.top <=0:
        enemy2.vy = 5    

    if enemy2.rect.bottom >=480:
        enemy2.vy = -5

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()