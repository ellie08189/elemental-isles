import pygame
import constants
from player import Player
from obstacle import Obstacle

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Circle Game")

# Create objects
player = Player(50, constants.GROUND_Y - constants.PLAYER_RADIUS)
obstacle = Obstacle(constants.SCREEN_WIDTH, constants.GROUND_Y - constants.OBSTACLE_RADIUS)
#cloud = pygame.image.load("assets/cloud.png")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player.apply_gravity()

    obstacle.update()
    obstacle.check_collision(player)

    # --- Drawing ---
    screen.fill(constants.BACKGROUND)
    pygame.draw.rect(screen, constants.GROUND_COLOR,
                     [0, constants.GROUND_Y, constants.SCREEN_WIDTH, 100])
    player.draw(screen)
    obstacle.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
