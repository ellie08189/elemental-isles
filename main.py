"""Main game loop for Legends of The Elemental Isles."""

# import necessary modules
import pygame
import constants
from character import Character
from character import Powers
from background import Background
from screens import PauseScreen
from screens import Score
from screens import TitleScreen
from screens import PlayButton
from screens import Name
from screens import GameOver
from screens import MapScreen
from screens import Victory
from screens import Buttons
from stationary_obstacles import Pillar
from stationary_obstacles import Bush1
from stationary_obstacles import Door
from platforms import PlatformManager
from moving_obstacles import Fireball
from moving_obstacles import Log
from key import Key
from key import TotalKeys
from lives import Lives

pygame.init()  # pylint: disable=no-member
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Legends of The Elemental Isles")

# Give the window time to initialize and gain focus
pygame.time.wait(100)
pygame.event.clear()  # Clear any events that happened during initialization

# Create objects
play = PlayButton()
name = Name()
background = Background()
background.sound_play()  # Play background music once at the start
character = Character(100, constants.GROUND_Y - constants.CHARACTER_HEIGHT)
power = Powers(character.x, character.y)

lives = Lives()
pillar = Pillar(
    constants.SCREEN_WIDTH,
    constants.GROUND_Y - constants.PILLAR_HEIGHT,
)
pillar.active = True  # Ensure the pillar is active at the start
pillar2 = Pillar(
    4500,
    constants.GROUND_Y - constants.PILLAR_HEIGHT,
)
pillar2.active = True
pillar3 = Pillar(6000, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar3.active = True
pillar4 = Pillar(8500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar4.active = True
pillar5 = Pillar(11500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar5.active = True
pillar6 = Pillar(14000, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar6.active = True
pillar7 = Pillar(17500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
pillar7.active = True

bush1 = Bush1(
    constants.SCREEN_WIDTH + 600,
    constants.GROUND_Y - constants.BUSH1_HEIGHT,
)
bush1.active = True
bush2 = Bush1(5250, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush2.active = True
bush3 = Bush1(9750, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush3.active = True
bush4 = Bush1(10750, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush4.active = True
bush5 = Bush1(13000, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush5.active = True
bush6 = Bush1(15000, constants.GROUND_Y - constants.BUSH1_HEIGHT)
bush6.active = True

platform_manager = PlatformManager()

fireball = Fireball(constants.SCREEN_WIDTH + 1000, 650)
fireball.active = True
log = Log(3250, constants.GROUND_Y - constants.LOG_HEIGHT)
log.active = True

key = Key(constants.SCREEN_WIDTH + 150, 250)
key.active = True
key2 = Key(4510, 250)
key2.active = True
key3 = Key(6010, 250)
key3.active = True
key4 = Key(8510, 250)
key4.active = True
key5 = Key(11510, 250)
key5.active = True
key6 = Key(14010, 250)
key6.active = True
key7 = Key(17510, 250)
key7.active = True

title_screen = TitleScreen()
game_over = GameOver()
map_screen = MapScreen()
pause_screen = PauseScreen()
door = Door(20000, constants.GROUND_Y - constants.DOOR_HEIGHT)
key_score = TotalKeys()
score = Score()
button = Buttons()

GAME_STATE = "title"
SCORE_PRINTED = False
keys = pygame.key.get_pressed()
EVENT = None

clock = pygame.time.Clock()
RUNNING = True
while RUNNING:
    for EVENT in pygame.event.get():
        if (
            EVENT.type == pygame.QUIT  # pylint: disable=no-member
            or EVENT.type == pygame.KEYDOWN  # pylint: disable=no-member
            and EVENT.key == pygame.K_ESCAPE  # pylint: disable=no-member
        ):
            RUNNING = False
            break  # Exit the event loop immediately to prevent further processing

        # switch between game states
        if GAME_STATE == "title":  # play button clicked changes screen to game screen
            mouse = pygame.mouse.get_pos()
            if 350 <= mouse[0] <= 650 and 260 <= mouse[1] <= 560:
                if EVENT.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                    GAME_STATE = "game"
        elif GAME_STATE == "game":
            if (
                pillar.collision_detected is True
                or pillar2.collision_detected is True
                or pillar3.collision_detected is True
                or pillar4.collision_detected is True
                or pillar5.collision_detected is True
                or pillar6.collision_detected is True
                or pillar7.collision_detected is True
            ):
                lives.lose_life(character)
                if lives.lives > 0:
                    pillar.collision_detected = False
                    pillar2.collision_detected = False
                    pillar3.collision_detected = False
                    pillar4.collision_detected = False
                    pillar5.collision_detected = False
                    pillar6.collision_detected = False
                    pillar7.collision_detected = False
                else:
                    GAME_STATE = "game_over"
            if (
                bush1.collision_detected is True
                or bush2.collision_detected is True
                or bush3.collision_detected is True
                or bush4.collision_detected is True
                or bush5.collision_detected is True
                or bush6.collision_detected is True
            ):
                lives.lose_life(character)
                if lives.lives > 0:
                    bush1.collision_detected = False
                    bush2.collision_detected = False
                    bush3.collision_detected = False
                    bush4.collision_detected = False
                    bush5.collision_detected = False
                    bush6.collision_detected = False
                else:
                    GAME_STATE = "game_over"
            if fireball.collision_detected is True:
                lives.lose_life(character)
                if lives.lives > 0:
                    fireball.collision_detected = False
                else:
                    GAME_STATE = "game_over"
            if log.collision_detected is True:
                lives.lose_life(character)
                if lives.lives > 0:
                    log.collision_detected = False
                else:
                    GAME_STATE = "game_over"
            if keys[pygame.K_a]:
                GAME_STATE = "map"
            if keys[pygame.K_SPACE]:
                GAME_STATE = "pause"
            if door.collision_detected is True:
                GAME_STATE = "victory"
        elif GAME_STATE == "game_over":
            game_over.draw(screen, score)
            mouse = pygame.mouse.get_pos()
        elif GAME_STATE == "pause":
            mouse = pygame.mouse.get_pos()
            if 350 <= mouse[0] <= 650 and 250 <= mouse[1] <= 550:
                if EVENT.type == pygame.MOUSEBUTTONUP or keys[pygame.K_SPACE]:
                    GAME_STATE = "game"
            else:
                GAME_STATE = "pause"
        elif GAME_STATE == "map":
            if keys[pygame.K_a]:
                GAME_STATE = "game"
        # error that any key pressed goes from map screen to game screen

    # calls appropriate methods based on game state
    if GAME_STATE == "title":
        title_screen.draw(screen)
        play.draw(screen)
        name.draw(screen)
    elif GAME_STATE == "game":

        keys = pygame.key.get_pressed()
        character.handle_input(keys, door)
        character.apply_gravity()
        character.update()

        power.power(character, keys)
        power.update()
        power.collision(fireball)

        pillar.update(keys, character)
        pillar.collision(character)
        pillar2.update(keys, character)
        pillar2.collision(character)
        pillar3.update(keys, character)
        pillar3.collision(character)
        pillar4.update(keys, character)
        pillar4.collision(character)
        pillar5.update(keys, character)
        pillar5.collision(character)
        pillar6.update(keys, character)
        pillar6.collision(character)
        pillar7.update(keys, character)
        pillar7.collision(character)

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

        platform_manager.update(keys, character, door)
        platform_manager.collision(character)

        fireball.update(background, character)
        fireball.collision(character)

        log.update(background)
        log.collision(character)

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
        key7.update(keys, character)
        key7.collision(character, key_score)

        door.update(keys, character)
        door.collision(character)
        button.update(keys, character)

        background.update(keys, character)
        background.approach_door(door)

        score.increase(power, key_score)

        background.draw(screen)
        door.draw(screen)
        character.draw(screen)
        power.draw(screen)
        pillar.draw(screen)
        pillar2.draw(screen)
        pillar3.draw(screen)
        pillar4.draw(screen)
        pillar5.draw(screen)
        pillar6.draw(screen)
        pillar7.draw(screen)

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
        key7.draw(screen)

        lives.draw(screen)
        score.draw(screen)
        button.draw(screen)

    elif GAME_STATE == "map":
        map_screen = MapScreen()
        map_screen.draw(screen)

    elif GAME_STATE == "pause":
        pause_screen = PauseScreen()
        pause_screen.draw(screen)

    elif GAME_STATE == "victory":
        victory_screen = Victory()
        victory_screen.score()
        victory_screen.score2(score)
        victory_screen.victory()
        victory_screen.keys_collected(key_score.cumulative_total)
        victory_screen.nextlevel()
        victory_screen.draw(screen)
        print(GAME_STATE)
        mouse = pygame.mouse.get_pos()
        if 380 <= mouse[0] <= 620 and 650 <= mouse[1] <= 680:
            if EVENT.type == pygame.MOUSEBUTTONUP:  # pylint: disable=no-member
                GAME_STATE = "title"

    elif GAME_STATE == "game_over":
        mouse = pygame.mouse.get_pos()
        if not SCORE_PRINTED:
            print("Fireballs destroyed " + str(power.collision_amount))
            print("Total keys collected: " + str(key_score.cumulative_total))
            print("Score = " + str(score.score))
            SCORE_PRINTED = True
        game_over.draw(screen, score)

        # Check if the mouse is within the specified range
        if 225 <= mouse[0] <= 335 and 460 <= mouse[1] <= 505:
            if EVENT.type == pygame.MOUSEBUTTONUP:  # pylint: disable=no-member
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
                    4500,
                    constants.GROUND_Y - constants.PILLAR_HEIGHT,
                )
                pillar2.active = True
                pillar3 = Pillar(6000, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar3.active = True
                pillar4 = Pillar(8500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar4.active = True
                pillar5 = Pillar(11500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar5.active = True
                pillar6 = Pillar(14000, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar6.active = True
                pillar7 = Pillar(17500, constants.GROUND_Y - constants.PILLAR_HEIGHT)
                pillar7.active = True

                bush1 = Bush1(
                    constants.SCREEN_WIDTH + 600,
                    constants.GROUND_Y - constants.BUSH1_HEIGHT,
                )
                bush1.active = True
                bush2 = Bush1(5250, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush2.active = True
                bush3 = Bush1(9750, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush3.active = True
                bush4 = Bush1(10750, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush4.active = True
                bush5 = Bush1(13000, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush5.active = True
                bush6 = Bush1(15000, constants.GROUND_Y - constants.BUSH1_HEIGHT)
                bush6.active = True

                fireball = Fireball(constants.SCREEN_WIDTH + 1000, 650)
                fireball.active = True

                log = Log(3250, constants.GROUND_Y - constants.LOG_HEIGHT)
                log.active = True

                platform_manager = PlatformManager()

                key = Key(constants.SCREEN_WIDTH + 150, 250)
                key.active = True
                key.amount = 0
                key2 = Key(4510, 250)
                key2.active = True
                key2.amount = 0
                key3 = Key(6010, 250)
                key3.active = True
                key3.amount = 0
                key4 = Key(8510, 250)
                key4.active = True
                key4.amount = 0
                key5 = Key(11510, 250)
                key5.active = True
                key5.amount = 0
                key6 = Key(14010, 250)
                key6.active = True
                key6.amount = 0
                key7 = Key(17510, 250)
                key7.active = True
                key7.amount = 0

                door = Door(20000, constants.GROUND_Y - constants.DOOR_HEIGHT)
                SCORE_PRINTED = False
                lives = Lives()
                lives.lives = 3
                score = Score()
                score.score = 0
                key_score.cumulative_total = 0
                GAME_STATE = "game"

        # exits the game when no is clicked
        if 600 <= mouse[0] <= 680 and 460 <= mouse[1] <= 505:
            if EVENT.type == pygame.MOUSEBUTTONUP:  # pylint: disable=no-member
                RUNNING = False
                break

    clock.tick(60)
    pygame.display.update()

pygame.quit()  # pylint: disable=no-member
