"""Main game loop."""

import pygame
from constants import WIDTH, HEIGHT, WHITE, FPS

# pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elemental Isles")
clock = pygame.time.Clock()


def main():
    """Run the game."""
    running = True
    game_over = False
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
