import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import UIElement
import title_screen
from US_STATE import *
from Agent import *
from GreedyAgent import *
from title_screen import *
import US_SCREEN
from US_SCREEN import *
import egypt_screen
from egypt_screen import *
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
    agent1 = Human("HUMAN", DARKRED)
    agent2 = PacifistAgent("PACIFIST", DARKRED)
    agent3 = GreedyAgent("GREEDY", DARKRED)
    agent4 = PassiveAgent("PASSIVE", DARKBLUE)
    agent5 = AgressiveAgent("AGGRESSIVE", DARKRED)
    # create super class for state
    random_state=US_STATE(None,None)
    while running:

        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = select_screen(screen,random_state)

        if game_state == GameState.QUIT:
            pygame.quit()
            break

        if(game_state== GameState.egypt):
            game_state = egypt_screen(screen)
        if (game_state == GameState.us):
            if(random_state.agent1 !=None and random_state.agent2!=None):
                game_state = us_screen(screen,random_state.agent1,random_state.agent2)
            else:
                print("PLEASE SELECT PLAYER")


    return

# call main when the script is run
if __name__ == "__main__":
    main()