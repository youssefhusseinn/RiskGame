import pygame
import pygame.freetype

from UIElement import *
import gamestate
from gamestate import GameState
import UIElement
from UIElement import *
import UISprite
import US_STATE
from US_STATE import *
import player
from player import *
import input_box
from input_box import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)

def us_screen(screen):

    countriesID = [(200, 50),(150, 150), (100, 300), (270, 170), (195, 300),
                   (380, 100), (410, 220), (315, 310), (300, 460), (565, 110),
                    (565, 200),(565, 280), (450, 340),(430, 470), (600, 370),
                    (620, 450),(600, 580), (700, 170),(720, 270), (730, 380),
                    (770, 500),(750, 570), (800, 200),(900, 170), (800, 320),
                    (880, 310),(950, 310), (1050, 350), (1050, 270), (1100, 200),
                    (1050, 425), (900, 445), (900, 530), (820, 530), (980, 530),
                    (1035, 490), (1035, 650)]

    state=US_STATE
    state.initializeState(state)
    element=UIElement
    return_btn = element.UIElement(
        center_position=(250, 700),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=BLACK,
        text="Return to main menu",
        id="0",
        country=None,
        action=GameState.TITLE

    )
    uiElements=[]
    i=0
    element= UIElement
    for country in countriesID:

        uiElements.append(element.UIElement(center_position= countriesID[i],
                                            font_size=30,
                                            bg_rgb=WHITE,
                                            text_rgb=state.countries[i].owner.color,
                                            text=str(state.countries[i].numOfTroops,),
                                            action=5,
                                            id=country,
                                            country=state.countries[i],
                                            ))
        i+=1
    while True:

        mouse_up = False
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        screen.fill(BLUE)
        usmapimage = pygame.image.load("assets/USMAP.png")
        screen.blit(usmapimage, (50, 0))



        for button in uiElements:
            ui_action = button.actionbutton(pygame.mouse.get_pos(), mouse_up,state,button.country)
            button.update_text(str(button.country.numOfTroops),button.country.owner.color)

            if ui_action is not None:

                return ui_action
            button.draw(screen)
        return_btn.draw(screen)
        MANUAL_CURSOR = pygame.image.load('assets/mouse.png').convert_alpha()
        screen.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))
        pygame.display.flip()

