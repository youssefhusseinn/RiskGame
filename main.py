import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import UIElement
import title_screen
from Agent import *
from GreedyAgent import *
from title_screen import *
import US_SCREEN
from US_SCREEN import *
import EG_SCREEN
from EG_SCREEN import *
import select_screen
from select_screen import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)


def main():
    pygame.init()

    screen = pygame.display.set_mode((1400, 750))

    game_state = GameState.TITLE
    running = True
    pygame.mouse.set_visible(False)  # hide the cursor
    MANUAL_CURSOR = pygame.image.load('assets/mouse.png').convert_alpha()
    screen.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))
    # create super class for state
    random_state=EG_STATE(None,None)
    while running:


        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = select_screen(screen,random_state)

        if game_state == GameState.QUIT:
            pygame.quit()
            break

        if(game_state== GameState.egypt):
            if (random_state.agent1 != None and random_state.agent2 != None and random_state.agent1.color != random_state.agent2.color):
                game_state = eg_screen(screen, random_state.agent1, random_state.agent2)
            else:
                ctypes.windll.user32.MessageBoxW(0, "PLEASE SELECT 2 DIFFERENT COLOR PLAYERS", 1)
                game_state = select_screen(screen, random_state)
                print("PLEASE SELECT PLAYER")



        if (game_state == GameState.us):
            if(random_state.agent1 !=None and random_state.agent2!=None and random_state.agent1.color != random_state.agent2.color ):
                game_state = us_screen(screen,random_state.agent1,random_state.agent2)
            else:
                ctypes.windll.user32.MessageBoxW(0, "PLEASE SELECT 2 DIFFERENT COLOR PLAYERS", 1)
                game_state = select_screen(screen, random_state)
                print("PLEASE SELECT PLAYER")


    return

# call main when the script is run
if __name__ == "__main__":
    main()