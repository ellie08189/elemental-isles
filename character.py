"""trying to represent a character in the game."""

import pygame


class Character:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.vy = 0
        self.on_ground = True
        self.idle_sprite = pygame.image.load("assets/idle1.png")
        self.walking_sprites = [
            pygame.image.load(f"assets/walk{i}.png")
            for i in range(1, 9)
            for _ in range(5)
        ]
        self.jump_sprites = [
            pygame.image.load(f"assets/jump{i}.png")
            for i in range(1, 9)
            for _ in range(5)
        ]
        self.sprites = [self.idle_sprite]
        self.max_index = 0
        self.current_index = 0
        self.is_walking = False
        self.is_jumping = False

    def walk(self, keys):
        """Switch between walking, jumping, and idle sprites based on key press."""
        if self.on_ground:
            if keys[pygame.K_UP]:
                self.vy = -10
                self.on_ground = False
                self.sprites = self.jump_sprites
                self.max_index = len(self.sprites) - 1
                self.current_index = 0
                self.is_jumping = True
                self.is_walking = False
            elif keys[pygame.K_RIGHT]:
                if not self.is_walking:
                    self.sprites = self.walking_sprites
                    self.max_index = len(self.sprites) - 1
                    self.current_index = 0
                    self.is_walking = True
                self.is_jumping = False
            else:
                if self.is_walking or self.is_jumping:
                    self.sprites = [self.idle_sprite]
                    self.max_index = 0
                    self.current_index = 0
                    self.is_walking = False
                    self.is_jumping = False
        else:
            # In air: keep jump animation
            if not self.is_jumping:
                self.sprites = self.jump_sprites
                self.max_index = len(self.sprites) - 1
                self.current_index = 0
                self.is_jumping = True

    def apply_gravity(self):
        self.vy += 1
        self.y += self.vy
        if self.y >= 100:  # Assuming ground level is at y = 100 for this example
            self.y = 100
            self.vy = 0
            self.on_ground = True
            # When landing, switch to idle sprite
            if self.is_jumping:
                self.sprites = [self.idle_sprite]
                self.max_index = 0
                self.current_index = 0
                self.is_jumping = False

    def update(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0

    def draw(self, screen):
        screen.blit(self.sprites[self.current_index], (self.x, self.y))


pygame.init()
pygame.display.set_caption("Character Animation Test")
character = Character(100, 100)
background = pygame.display.set_mode((400, 300))
background.fill((255, 255, 255))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break  # Exit the event loop immediately to prevent further processing
    keys = pygame.key.get_pressed()
    character.walk(keys)
    character.apply_gravity()
    character.update()
    background.fill((255, 255, 255))
    character.draw(background)
    clock.tick(60)
    pygame.display.update()

pygame.quit()
