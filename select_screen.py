import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIelement
from UIelement import *
import main
from main import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)

def select_screen(screen):
    element = UIelement

    return_btn = element.UIElement(
        center_position=(300, 700),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        id=0,
        country=None,

        action=GameState.TITLE,
    )
    egypt_btn = element.UIElement(
        center_position=(375,550 ),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="EGYPT",
        id=1,
        country=None,

        action=GameState.egypt,
    )
    us_btn = element.UIElement(
        center_position=(950, 550),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="UNITED STATE",
        id=2,
        country=None,

        action=GameState.us,
    )
    buttons=[return_btn,egypt_btn,us_btn]
    egyptmapimage = pygame.image.load('assets/egyptmapchoice.png')
    usmapimage = pygame.image.load('assets/usmapchoice.png')
    image4 = pygame.image.load('assets/choosemap.png')





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
        screen.blit(egyptmapimage, (250, 200))
        screen.blit(usmapimage, (800, 230))
        screen.blit(image4, (400, 0))


        pygame.display.flip()
