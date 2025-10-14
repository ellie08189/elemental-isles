import pygame
import constants
import math


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = constants.OBSTACLE_RADIUS
        self.color = constants.OBSTACLE_COLOR
        self.speed = constants.OBSTACLE_SPEED
        self.active = True

    def update(self):
        if self.active:
            self.x += self.speed
            if self.x + self.radius < 0:  # respawn on right
                self.speed -= 1
                if self.speed < -20:
                    self.speed = -20
                self.x = constants.SCREEN_WIDTH
                self.active = True

    def check_collision(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.sqrt(dx * dx + dy * dy)
        min_distance = self.radius + player.radius
        if distance < min_distance:
            # Calculate overlap
            overlap = min_distance - distance
            # Determine direction based on player movement
            if player.x > self.x and player.speed > 0:
                # Player moving right, push left
                player.x += overlap
            elif player.x < self.x and player.speed > 0:
                # Player moving left, push right
                player.x -= overlap
            # Optionally, you can also handle vertical movement if needed
            elif player.y < self.y and player.speed > 0:
                player.y -= overlap
            elif player.y > self.y and player.speed > 0:
                player.y += overlap
            self.active = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
