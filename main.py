"""Main game loop for Legends of The Elemental Isles."""

# import necessary modules
import pygame
import constants
from character import Character
from character import Powers
from background import Background
from screens import PauseScreen
from screens import TitleScreen
from screens import PlayButton
from screens import GameOver
from screens import MapScreen
from stationary_obstacles import Pillar
from platforms import PlatformManager
from stationary_obstacles import Bush1
from moving_obstacles import Fireball
from moving_obstacles import Log
from key import Key
from key import TotalKeys

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Legends of The Elemental Isles")

# Give the window time to initialize and gain focus
pygame.time.wait(100)
pygame.event.clear()  # Clear any events that happened during initialization

# Create objects
play = PlayButton()
background = Background()
# background.sound_play()  # Play background music once at the start
character = Character(100, constants.GROUND_Y - constants.CHARACTER_HEIGHT)
power = Powers(character.x, character.y)

pillar = Pillar(
    constants.SCREEN_WIDTH,
    constants.GROUND_Y - constants.PILLAR_HEIGHT,
)
pillar.active = True  # Ensure the pillar is active at the start
pillar2 = Pillar(
    constants.SCREEN_WIDTH + 2500,
    constants.GROUND_Y - constants.PILLAR_HEIGHT,
)
pillar2.active = True
pillar3 = Pillar(5750, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar3.active = True
pillar4 = Pillar(7500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar4.active = True
pillar5 = Pillar(9000, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar5.active = True
pillar6 = Pillar(10500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar6.active = True

bush1 = Bush1(
    constants.SCREEN_WIDTH + 600,
    constants.GROUND_Y - constants.BUSH1_HEIGHT,
)
bush1.active = True
bush2 = Bush1(8000, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush2.active = True
bush3 = Bush1(4500, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush3.active = True
bush4 = Bush1(5250, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush4.active = True
bush5 = Bush1(6500, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush5.active = True
bush6 = Bush1(7500, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush6.active = True

platform_manager = PlatformManager()

fireball = Fireball(constants.SCREEN_WIDTH + 1000, 650)
fireball.active = True
log = Log(3250, constants.GROUND_Y - constants.LOG_HEIGHT)
log.active = True

key = Key(constants.SCREEN_WIDTH + 150, 250)
key2 = Key(constants.SCREEN_WIDTH + 2500, 250)
key.active = True
key2.active = True
key3 = Key(5750, 250)
key3.active = True
key4 = Key(7500, 250)
key4.active = True
key5 = Key(9000, 250)
key5.active = True
key6 = Key(10500, 250)
key6.active = True

title_screen = TitleScreen()
game_over = GameOver()
map_screen = MapScreen()
pause_screen = PauseScreen()

key_score = TotalKeys()

game_state = "title"
score_printed = False

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            running = False
            break  # Exit the event loop immediately to prevent further processing

        # switch between game states
        if game_state == "title":  # play button clicked changes screen to game screen
            mouse = pygame.mouse.get_pos()
            if 350 <= mouse[0] <= 650 and 250 <= mouse[1] <= 550:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "game"
        elif game_state == "game":
            if (
                pillar.collision_detected is True
                or pillar2.collision_detected is True
                or pillar3.collision_detected is True
                or pillar4.collision_detected is True
                or pillar5.collision_detected is True
                or pillar6.collision_detected is True
            ):
                game_state = "game_over"
            if (
                bush1.collision_detected is True
                or bush2.collision_detected is True
                or bush3.collision_detected is True
                or bush4.collision_detected is True
                or bush5.collision_detected is True
                or bush6.collision_detected is True
            ):
                game_state = "game_over"
            if fireball.collision_detected is True:
                game_state = "game_over"
            if log.collision_detected is True:
                game_state = "game_over"
            if keys[pygame.K_a]:
                game_state = "map"
            if keys[pygame.K_SPACE]:
                game_state = "pause"
        elif game_state == "game_over":
            game_over.draw(screen)
            mouse = pygame.mouse.get_pos()
        elif game_state == "pause":
            mouse = pygame.mouse.get_pos()
            if 350 <= mouse[0] <= 650 and 250 <= mouse[1] <= 550:
                if event.type == pygame.MOUSEBUTTONUP or keys[pygame.K_SPACE]:
                    game_state = "game"
            else:
                game_state = "pause"
        elif game_state == "map":
            if keys[pygame.K_a]:
                game_state = "game"
        # error that any key pressed goes from map screen to game screen

    # calls appropriate methods based on game state
    if game_state == "title":
        title_screen.draw(screen)
        play.draw(screen)
    elif game_state == "game":

        keys = pygame.key.get_pressed()
        character.handle_input(keys)
        character.apply_gravity()
        character.update()

        power.power(character, keys)
        power.update()
        power.collision(fireball)

        pillar.update(keys, character, bush1)
        pillar.collision(character)
        pillar2.update(keys, character, bush1)
        pillar2.collision(character)
        pillar3.update(keys, character, bush1)
        pillar3.collision(character)
        pillar4.update(keys, character, bush1)
        pillar4.collision(character)
        pillar5.update(keys, character, bush1)
        pillar5.collision(character)
        pillar6.update(keys, character, bush1)
        pillar6.collision(character)

        bush1.update(keys, character)
        bush1.collision(character)
        bush2.update(keys, character)
        bush2.collision(character)
        bush3.update(keys, character)
        bush3.collision(character)
        bush4.update(keys, character)
        bush4.collision(character)
        bush5.update(keys, character)
        bush5.collision(character)
        bush6.update(keys, character)
        bush6.collision(character)

        platform_manager.update(keys, character)
        platform_manager.collision(character)

        fireball.update(background, character)
        # fireball.collision(character)

        log.update(background, character)
        # log.collision(character)

        key.update(keys, character)
        key.collision(character, key_score)
        key2.update(keys, character)
        key2.collision(character, key_score)
        key3.update(keys, character)
        key3.collision(character, key_score)
        key4.update(keys, character)
        key4.collision(character, key_score)
        key5.update(keys, character)
        key5.collision(character, key_score)
        key6.update(keys, character)
        key6.collision(character, key_score)

        background.update(keys, character)

        background.draw(screen)
        character.draw(screen)
        power.draw(screen)
        pillar.draw(screen)
        pillar2.draw(screen)
        pillar3.draw(screen)
        pillar4.draw(screen)
        pillar5.draw(screen)
        pillar6.draw(screen)

        bush1.draw(screen)
        bush2.draw(screen)
        bush3.draw(screen)
        bush4.draw(screen)
        bush5.draw(screen)
        bush6.draw(screen)

        platform_manager.draw(screen)
        fireball.draw(screen)
        log.draw(screen)

        key.draw(screen)
        key2.draw(screen)
        key3.draw(screen)
        key4.draw(screen)
        key5.draw(screen)
        key6.draw(screen)

    elif game_state == "map":
        map_screen = MapScreen()
        map_screen.draw(screen)

    elif game_state == "pause":
        pause_screen = PauseScreen()
        pause_screen.draw(screen)

    elif game_state == "game_over":
        mouse = pygame.mouse.get_pos()
        if not score_printed:
            print("Fireballs destroyed " + str(power.collision_amount))
            print("Total keys collected: " + str(key_score.total))
            print(
                "Score = "
                + str(((key_score.total) * 100) + (power.collision_amount * 50))
            )
            score_printed = True
        game_over.draw(screen)

        # Check if the mouse is within the specified range
        if 225 <= mouse[0] <= 335 and 460 <= mouse[1] <= 505:
            if event.type == pygame.MOUSEBUTTONUP:
                # Reset player and pillar to restart the game
                character = Character(
                    100, constants.GROUND_Y - constants.CHARACTER_HEIGHT
                )
                power = Powers(character.x, character.y)

                pillar = Pillar(
                    constants.SCREEN_WIDTH,
                    constants.GROUND_Y - constants.PILLAR_HEIGHT,
                )
                pillar.active = True  # Ensure the pillar is active
                pillar2 = Pillar(
                    constants.SCREEN_WIDTH + 2500,
                    constants.GROUND_Y - constants.PILLAR_HEIGHT,
                )
                pillar2.active = True
                pillar3 = Pillar(5750, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar3.active = True
                pillar4 = Pillar(7500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar4.active = True
                pillar5 = Pillar(9000, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar5.active = True
                pillar6 = Pillar(10500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar6.active = True

                bush1 = Bush1(
                    constants.SCREEN_WIDTH + 600,
                    constants.GROUND_Y - constants.BUSH1_HEIGHT,
                )
                bush1.active = True
                bush2 = Bush1(8000, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush2.active = True
                bush3 = Bush1(4500, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush3.active = True
                bush4 = Bush1(5250, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush4.active = True
                bush5 = Bush1(6500, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush5.active = True
                bush6 = Bush1(7500, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush6.active = True

                fireball = Fireball(constants.SCREEN_WIDTH + 1000, 650)
                fireball.active = True
                log = Log(3250, constants.GROUND_Y - constants.LOG_HEIGHT)
                log.active = True
                platform_manager = PlatformManager()
                key = Key(constants.SCREEN_WIDTH + 150, 250)
                key.active = True
                key.amount = 0
                key2 = Key(constants.SCREEN_WIDTH + 2500, 250)
                key2.active = True
                key2.amount = 0
                key3 = Key(5750, 250)
                key3.active = True
                key3.amount = 0
                key4 = Key(7500, 250)
                key4.active = True
                key4.amount = 0
                key5 = Key(9000, 250)
                key5.active = True
                key5.amount = 0
                key6 = Key(10500, 250)
                key6.active = True
                key6.amount = 0
                key_score.total = 0
                score_printed = False
                game_state = "game"

        # exits the game when no is clicked
        if 600 <= mouse[0] <= 680 and 460 <= mouse[1] <= 505:
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
                break

    clock.tick(60)
    pygame.display.update()

pygame.quit()
