import pygame
import random
from player import Player
from enemy import Enemy
from collectible import Collectible
from bullet import Bullet

# Initialize pygame
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

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

# Fonts
font_large = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# Game states
START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"
game_state = START

# Create instances
player = Player()
enemy1 = Enemy("enemy1.png", 3)
enemy2 = Enemy("enemy2.png", 5, (600, 0))
collectible = Collectible()
score = 0

all_sprites = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
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


bullets = []

# Start menu
def draw_start_menu():
    screen.blit(background, (0, 0))
    title_text = font_large.render("2D Game", True, (255, 255, 255))
    start_text = font_small.render("Press SPACE to start", True, (255, 255, 255))
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - 50))
    screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2 + 50))

# Game over menu
def draw_game_over_menu():
    screen.blit(background, (0, 0))
    game_over_text = font_large.render("Game Over", True, (255, 255, 255))
    score_text = font_small.render(f"Score: {score}", True, (255, 255, 255))
    restart_text = font_small.render("Press SPACE to restart", True, (255, 255, 255))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 50))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 50))

# Main game loop
while running:
    playerPos = pygame.math.Vector2(*player.rect.center)
    mousePos = pygame.math.Vector2(*pygame.mouse.get_pos())
    direction = (mousePos - playerPos).normalize()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == START:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING
            elif game_state == PLAYING:
                player.handle_input(event.key, True)
            elif game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    # Reset game state
                    player.reset()
                    enemy1.reset()
                    enemy2.reset()
                    collectible.reset()
                    bullets = []
                    bullets_group.empty()
                    score = 0
                    game_state = PLAYING
        elif event.type == pygame.KEYUP and game_state == PLAYING:
            player.handle_input(event.key, False)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            scaled_direction = direction * 10
            bullet = Bullet(*player.rect.center,
                scaled_direction.x, scaled_direction.y,
                direction.rotate(90).angle_to((0, 0)))
            bullets_group.add(bullet)
            bullets.append(bullet)

    if game_state == START:
        draw_start_menu()
    elif game_state == PLAYING:
        all_sprites.update()
        screen.blit(background, (0, 0))

        player.collisions(enemies, collectible)

        if player.lives <= 0:
            game_state = GAME_OVER
            collide.play()

        if player.rect.colliderect(collectible.rect):
                score += 1
                print(score)
                if not channel2.get_busy():
                    collect.play()
                collectible.rect.x = random.randint(0,580)
                collectible.rect.y = random.randint(0,400)
        
        for enemy in enemies:
            enemy.collisions(bullets)

        for bullet in bullets:
            bullet.update()

        # Draw all sprites
        all_sprites.draw(screen)
        bullets_group.draw(screen)
        # Draw score
        score_text = font_small.render(f"Score: {score}", True, (255, 255, 255))
        pygame.draw.line(screen,pygame.Color(255,255,255),playerPos, playerPos + direction * 50)
        screen.blit(score_text, (10, 10))

    elif game_state == GAME_OVER:
        draw_game_over_menu()


    pygame.draw.circle(screen, pygame.Color(255,255,255), mousePos,3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()