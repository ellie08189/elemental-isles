"""Main game loop."""

import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Hello Pygame")
background = (189, 244, 250)
screen.fill(background)
pygame.display.flip()

# draw shape
pygame.draw.rect(screen, (72, 201, 32), [0, 700, 1000, 100], 0)
pygame.draw.circle(screen, (255, 0, 0), [50, 650], 50, 0)
pygame.display.update()  # draws on screen

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
