from tkinter.tix import PopupMenu

import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIElement
from UIElement import *
import main
from main import *
import gamestate
from gamestate import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)

def select_screen(screen,state):
    element = UIElement

    return_btn = element.UIElement(
        center_position=(300, 700),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        id=0,
        action=GameState.TITLE,
    )
    egypt_btn = element.UIElement(
        center_position=(375,450 ),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="EGYPT",
        id=1,
        action=GameState.egypt,
    )
    us_btn = element.UIElement(
        center_position=(950, 450),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="UNITED STATE",
        id=2,
        action=GameState.us,
    )
    buttons=[return_btn,egypt_btn,us_btn]
    egyptmapimage = pygame.image.load('assets/egyptmapchoice.png')
    usmapimage = pygame.image.load('assets/usmapchoice.png')
    image4 = pygame.image.load('assets/choosemap.png')
    human_btn = element.UIElement(
        center_position=(100, 525),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKRED,
        text="HUMAN",
        id=2,
        action=0,
    )
    passive_btn = element.UIElement(
        center_position=(250, 525),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKRED,
        text="PASSIVE",
        id=2,
        action=0,
    )
    agressive_btn = element.UIElement(
        center_position=(450, 525),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKRED,
        text="AGRESSIVE",
        id=2,
        action=0,
    )
    pacifist_btn = element.UIElement(
        center_position=(650, 525),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKRED,
        text="PACIFIST",
        id=2,
        action=0,
    )
    greedy_btn = element.UIElement(
        center_position=(850, 525),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKRED,
        text="GREEDY",
        id=2,
        action=0,
    )
    miniMax_btn = element.UIElement(
        center_position=(1050, 525),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKRED,
        text="MINIMAX",
        id=2,
        action=0,
    )
    human_btn2 = element.UIElement(
        center_position=(100,575),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKBLUE,
        text="HUMAN",
        id=2,
        action=0,
    )
    passive_btn2 = element.UIElement(
        center_position=(250, 575),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKBLUE,
        text="PASSIVE",
        id=2,
        action=0,
    )
    agressive_btn2 = element.UIElement(
        center_position=(450, 575),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKBLUE,
        text="AGRESSIVE",
        id=2,
        action=0,
    )
    pacifist_btn2 = element.UIElement(
        center_position=(650, 575),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKBLUE,
        text="PACIFIST",
        id=2,
        action=0,
    )
    greedy_btn2 = element.UIElement(
        center_position=(850, 575),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKBLUE,
        text="GREEDY",
        id=2,
        action=0,
    )
    miniMax_btn2 = element.UIElement(
        center_position=(1050, 575),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=DARKBLUE,
        text="MINIMAX",
        id=2,
        action=0,
    )
    selection_buttons=[human_btn,pacifist_btn,passive_btn,greedy_btn,agressive_btn,miniMax_btn,
                       human_btn2,pacifist_btn2,passive_btn2,greedy_btn2,agressive_btn2,miniMax_btn2]
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
        for button in selection_buttons:

            ui_action = button.update_select(pygame.mouse.get_pos(), mouse_up,button.text,button.text_rgb,state)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        screen.blit(egyptmapimage, (250, 150))
        screen.blit(usmapimage, (800, 180))
        screen.blit(image4, (400, 0))
        MANUAL_CURSOR = pygame.image.load('assets/mouse.png').convert_alpha()
        screen.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))

        pygame.display.flip()
