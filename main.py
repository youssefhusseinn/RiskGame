import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import UIelement
import title_screen
from title_screen import *
import us_screen
from us_screen import *
import egypt_screen
from egypt_screen import *
import select_screen
from select_screen import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

def main():
    pygame.init()

    screen = pygame.display.set_mode((1400, 750))

    game_state = GameState.TITLE
    running=True
    while running:

            if game_state == GameState.TITLE:
                game_state = title_screen(screen)

            if game_state == GameState.NEWGAME:
                game_state = select_screen(screen)

            if game_state == GameState.QUIT:
                pygame.quit()

            if(game_state== GameState.egypt):
                game_state = egypt_screen(screen)
            if (game_state == GameState.us):
                game_state = us_screen(screen)

    return

# call main when the script is run
if __name__ == "__main__":
    main()