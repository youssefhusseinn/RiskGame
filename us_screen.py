import pygame
import pygame.freetype

from UIelement import *
import gamestate
from gamestate import GameState
import UIelement
from UIelement import *
import UISprite
from UISprite import *
from UISprite import UISprite
BLUE = (9, 5, 101)
WHITE = (255, 255, 255,0)
BLACK=(0,0,0)
def us_screen(screen):

    element = UIelement
    sprite= UISprite
    text="0"

    return_btn = element.UIElement(
        center_position=(140, 700),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE
    )
    country_us_1 = element.UIElement(
        center_position=(200, 50),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="1",
        action=None
    )
    country_us_2 = element.UIElement(
        center_position=(150, 150),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="2",
        action=None
    )
    country_us_3 = element.UIElement(
        center_position=(100, 300),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="3",
        action=None
    )
    country_us_4 = element.UIElement(
        center_position=(270, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="4",
        action=None
    )
    country_us_5 = element.UIElement(
        center_position=(195, 300),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="5",
        action=None
    )
    country_us_6= element.UIElement(
        center_position=(380, 100),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="6",
        action=None
    )
    country_us_7 = element.UIElement(
        center_position=(410, 220),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="7",
        action=None
    )
    country_us_8 = element.UIElement(
        center_position=(315, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="8",
        action=None
    )
    country_us_9 = element.UIElement(
        center_position=(300, 460),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="9",
        action=None
    )
    country_us_10 = element.UIElement(
        center_position=(565, 110),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="10",
        action=None
    )
    country_us_11 = element.UIElement(
        center_position=(565, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="11",
        action=None
    )
    country_us_12 = element.UIElement(
        center_position=(565, 280),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="12",
        action=None
    )
    country_us_13 = element.UIElement(
        center_position=(450, 340),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="13",
        action=None
    )
    country_us_14 = element.UIElement(
        center_position=(430, 470),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="14",
        action=None
    )
    country_us_15 = element.UIElement(
        center_position=(600, 370),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="15",
        action=None
    )
    country_us_16 = element.UIElement(
        center_position=(620, 450),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="16",
        action=None
    )
    country_us_17 = element.UIElement(
        center_position=(600, 580),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="17",
        action=None
    )
    country_us_18 = element.UIElement(
        center_position=(700, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="18",
        action=None
    )
    country_us_19 = element.UIElement(
        center_position=(720, 270),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="19",
        action=None
    )
    country_us_20 = element.UIElement(
        center_position=(730, 380),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="20",
        action=None
    )
    country_us_21 = element.UIElement(
        center_position=(750, 480),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="21",
        action=None
    )
    country_us_22 = element.UIElement(
        center_position=(750, 570),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="22",
        action=None
    )

    country_us_23 = element.UIElement(
        center_position=(800, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="23",
        action=None
    )
    country_us_24 = element.UIElement(
        center_position=(900, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="24",
        action=None
    )
    country_us_25 = element.UIElement(
        center_position=(800, 320),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="25",
        action=None
    )
    country_us_26 = element.UIElement(
        center_position=(880, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="26",
        action=None
    )
    country_us_27 = element.UIElement(
        center_position=(950, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="27",
        action=None
    )
    country_us_28 = element.UIElement(
        center_position=(1050, 350),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="28",
        action=None
    )
    country_us_29 = element.UIElement(
        center_position=(1050, 270),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="29",
        action=None
    )
    country_us_30 = element.UIElement(
        center_position=(1100, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="30",
        action=None
    )
    country_us_31 = element.UIElement(
        center_position=(1050, 425),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="31",
        action=None
    )
    country_us_32 = element.UIElement(
        center_position=(900, 445),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="32",
        action=None
    )
    country_us_33 = element.UIElement(
        center_position=(900, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="33",
        action=None
    )
    country_us_34 = element.UIElement(
        center_position=(820, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="34",
        action=None
    )
    country_us_35 = element.UIElement(
        center_position=(980, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="35",
        action=None
    )
    country_us_36 = element.UIElement(
        center_position=(1035, 490),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="36",
        action=None
    )
    country_us_37 = element.UIElement(
        center_position=(1035, 650),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="37",
        action=None
    )
    usmapimage = pygame.image.load(r'.\assets\USMAP.png')
    buttons = [return_btn,
               country_us_1,country_us_2,country_us_3,
               country_us_4,country_us_5,country_us_6,
               country_us_7,country_us_8,country_us_9,
               country_us_10,country_us_11,country_us_12,
               country_us_13,country_us_14,country_us_15,
               country_us_16,country_us_17,country_us_18,
               country_us_19,country_us_20,country_us_21,
               country_us_22,country_us_23,country_us_24,
               country_us_25,country_us_26,country_us_27,
               country_us_28,country_us_29,country_us_30,
               country_us_31,country_us_32,country_us_33,
               country_us_34,country_us_35,country_us_36,country_us_37]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)
        screen.blit(usmapimage,(50,0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)


        pygame.display.flip()
