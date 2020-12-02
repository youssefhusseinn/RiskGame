import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIelement
from UIelement import *
import gamestate
from gamestate import GameState
BLUE = (9, 5, 101)
WHITE = (255, 255, 255,0)
BLACK=(0,0,0)
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)
def egypt_screen(screen):
    element= UIelement
    return_btn = element.UIElement(
        center_position=(150, 720),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        id="0",
        action=GameState.TITLE,
    )

    country_eg_1 = element.UIElement(
        center_position=(240, 142),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg1",
        action=None
    )
    country_eg_2 = element.UIElement(
        center_position=(380, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg2",
        action=None
    )
    country_eg_3 = element.UIElement(
        center_position=(485, 265),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg3",
        action=None
    )
    country_eg_4 = element.UIElement(
        center_position=(650, 268),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg4",
        action=None
    )
    country_eg_5 = element.UIElement(
        center_position=(626.5, 235),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg5",
        action=None
    )
    country_eg_6 = element.UIElement(
        center_position=(677, 201),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg6",
        action=None
    )
    country_eg_7 = element.UIElement(
        center_position=(650, 113),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg7",
        action=None
    )
    country_eg_8 = element.UIElement(
        center_position=(597, 101),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg8",
        action=None
    )
    country_eg_9 = element.UIElement(
        center_position=(720, 65),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg9",
        action=None
    )
    country_eg_10 = element.UIElement(
        center_position=(726, 114),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg10",
        action=None
    )
    country_eg_11 = element.UIElement(
        center_position=(773, 81),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg11",
        action=None
    )
    country_eg_12 = element.UIElement(
        center_position=(787, 117),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg12",
        action=None
    )
    country_eg_13 = element.UIElement(
        center_position=(785, 177),
        font_size=35,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg13",
        action=None
    )
    country_eg_14 = element.UIElement(
        center_position=(864, 112),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg14",
        action=None
    )
    country_eg_15 = element.UIElement(
        center_position=(861, 178),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg15",
        action=None
    )
    country_eg_16 = element.UIElement(
        center_position=(1011, 105),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg16",
        action=None
    )
    country_eg_17 = element.UIElement(
        center_position=(1011, 204),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg17",
        action=None
    )
    country_eg_18 = element.UIElement(
        center_position=(832, 325),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg18",
        action=None
    )
    country_eg_19 = element.UIElement(
        center_position=(735, 340),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg19",
        action=None
    )
    country_eg_20 = element.UIElement(
        center_position=(800, 388),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg20",
        action=None
    )
    country_eg_21 = element.UIElement(
        center_position=(910, 426),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg21",
        action=None
    )
    country_eg_22 = element.UIElement(
        center_position=(918, 592),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="0",
        id="eg22",
        action=None
    )
    buttons = [country_eg_1, country_eg_2, country_eg_3,
               country_eg_4, country_eg_5, country_eg_6,
               country_eg_7, country_eg_8, country_eg_9,
               country_eg_10, country_eg_11, country_eg_12,
               country_eg_13, country_eg_14, country_eg_15,
               country_eg_16, country_eg_17, country_eg_18,
               country_eg_19, country_eg_20, country_eg_21,
               country_eg_22,return_btn]
    image = pygame.image.load('assets/egyptmapgame.png')




    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)
        screen.blit(image, (75, 50))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            # button.set_text(button.id)
            #
            button.update_text(button.text, DARKBLUE)
            if ui_action is not None:
                return ui_action
            button.draw(screen)



        pygame.display.flip()
