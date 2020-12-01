import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIelement
from UIelement import *
import gamestate
from gamestate import GameState
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)


def title_screen(screen):
    element = UIelement

    start_btn = element.UIElement(
        center_position=(700, 400),
        font_size=70,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="START",
        id=0,
        action=GameState.NEWGAME,
    )
    quit_btn = element.UIElement(
        center_position=(700, 500),
        font_size=70,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="QUIT",
        id=1,
        action=GameState.QUIT
    )
    buttons = [start_btn, quit_btn]
    titleimage = pygame.image.load('assets/gamename.png')


    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        screen.blit(titleimage, (350, 50))

        pygame.display.flip()
