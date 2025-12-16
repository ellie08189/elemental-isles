"""trying to represent a character in the game."""

import pygame
import constants


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.vy = 0
        self.on_ground = True
        self.idle_sprite = constants.IDLE
        self.walking_sprites = constants.WALKING
        self.walkback_sprites = constants.WALKBACK
        self.sprites = [self.idle_sprite]
        self.max_index = 0
        self.current_index = 0
        # self.is_walking = False
        # self.is_jumping = False

    def handle_input(self, keys):
        """Switch between walking, jumping, and idle sprites based on key press."""
        if keys[pygame.K_RIGHT]:
            self.sprites = self.walking_sprites
            self.max_index = len(self.sprites) - 1
            if self.x != constants.SCREEN_WIDTH // 2:
                self.x += self.speed

        elif keys[pygame.K_LEFT]:
            self.sprites = self.walkback_sprites
            self.max_index = len(self.sprites) - 1
            if self.x != constants.SCREEN_WIDTH // 2:
                self.x -= self.speed
        else:
            self.sprites = [self.idle_sprite]
            self.max_index = 0
            self.current_index = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.vy = constants.JUMP_STRENGTH
            self.on_ground = False
            self.max_index = len(self.sprites) - 1
            self.current_index = 0

    def apply_gravity(self):
        self.vy += constants.GRAVITY
        self.y += self.vy
        if (
            self.y >= constants.GROUND_Y - constants.CHARACTER_HEIGHT
        ):  # Assuming ground level is at y = 100 for this example
            self.y = constants.GROUND_Y - constants.CHARACTER_HEIGHT
            self.vy = 0
            self.on_ground = True

    def update(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0

    def draw(self, screen):
        screen.blit(self.sprites[self.current_index], (self.x, self.y))


# pygame.init()
# pygame.display.set_caption("Character Animation Test")
# character = Character(100, constants.GROUND_Y - constants.CHARACTER_HEIGHT)
# background = pygame.display.set_mode((1000, 800))
# background.fill((255, 255, 255))
# clock = pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             break  # Exit the event loop immediately to prevent further processing
#     keys = pygame.key.get_pressed()
#     character.handle_input(keys)
#     character.apply_gravity()
#     character.update()
#     background.fill((255, 255, 255))
#     character.draw(background)
#     clock.tick(60)
#     pygame.display.update()

# pygame.quit()
