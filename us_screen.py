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
import USGame
from USGame import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255,0)
BLACK=(0,0,0)
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)
def us_screen(screen):

    element = UIelement
    state= USGame()
    sprite= UISprite
    text="0"
    return_btn = element.UIElement(
        center_position=(250, 700),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=BLACK,
        text="Return to main menu",
        id="0",
        action=GameState.TITLE
    )
    country_us_1 = element.UIElement(
        center_position=(200, 50),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="1",
        id="us1",
        action=None
    )
    country_us_2 = element.UIElement(
        center_position=(150, 150),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="2",
        id="us2",
        action=None
    )
    country_us_3 = element.UIElement(
        center_position=(100, 300),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="3",
        id="us3",
        action=None
    )
    country_us_4 = element.UIElement(
        center_position=(270, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="4",
        id="us4",
        action=None
    )
    country_us_5 = element.UIElement(
        center_position=(195, 300),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="5",
        id="us5",
        action=None
    )
    country_us_6= element.UIElement(
        center_position=(380, 100),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="6",
        id="us6",
        action=None
    )
    country_us_7 = element.UIElement(
        center_position=(410, 220),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="7",
        id="us7",
        action=None
    )
    country_us_8 = element.UIElement(
        center_position=(315, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="8",
        id="us8",
        action=None
    )
    country_us_9 = element.UIElement(
        center_position=(300, 460),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="9",
        id="us9",
        action=None
    )
    country_us_10 = element.UIElement(
        center_position=(565, 110),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="10",
        id="us10",
        action=None
    )
    country_us_11 = element.UIElement(
        center_position=(565, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="11",
        id="us11",
        action=None
    )
    country_us_12 = element.UIElement(
        center_position=(565, 280),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="12",
        id="us12",
        action=None
    )
    country_us_13 = element.UIElement(
        center_position=(450, 340),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="13",
        id="us13",
        action=None
    )
    country_us_14 = element.UIElement(
        center_position=(430, 470),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="14",
        id="us14",
        action=None
    )
    country_us_15 = element.UIElement(
        center_position=(600, 370),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="15",
        id="us15",
        action=None
    )
    country_us_16 = element.UIElement(
        center_position=(620, 450),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="16",
        id="us16",
        action=None
    )
    country_us_17 = element.UIElement(
        center_position=(600, 580),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="17",
        id="us17",
        action=None
    )
    country_us_18 = element.UIElement(
        center_position=(700, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="18",
        id="us18",
        action=None
    )
    country_us_19 = element.UIElement(
        center_position=(720, 270),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="19",
        id="us19",
        action=None
    )
    country_us_20 = element.UIElement(
        center_position=(730, 380),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="20",
        id="us20",
        action=None
    )
    country_us_21 = element.UIElement(
        center_position=(750, 480),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="21",
        id="us21",
        action=None
    )
    country_us_22 = element.UIElement(
        center_position=(750, 570),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="22",
        id="us22",
        action=None
    )

    country_us_23 = element.UIElement(
        center_position=(800, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="23",
        id="us23",
        action=None
    )
    country_us_24 = element.UIElement(
        center_position=(900, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="24",
        id="us24",
        action=None
    )
    country_us_25 = element.UIElement(
        center_position=(800, 320),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="25",
        id="us25",
        action=None
    )
    country_us_26 = element.UIElement(
        center_position=(880, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="26",
        id="us26",
        action=None
    )
    country_us_27 = element.UIElement(
        center_position=(950, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="27",
        id="us27",
        action=None
    )
    country_us_28 = element.UIElement(
        center_position=(1050, 350),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="28",
        id="us28",
        action=None
    )
    country_us_29 = element.UIElement(
        center_position=(1050, 270),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="29",
        id="us29",
        action=None
    )
    country_us_30 = element.UIElement(
        center_position=(1100, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="30",
        id="us30",
        action=None
    )
    country_us_31 = element.UIElement(
        center_position=(1050, 425),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="31",
        id="us31",
        action=None
    )
    country_us_32 = element.UIElement(
        center_position=(900, 445),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="32",
        id="us32",
        action=None
    )
    country_us_33 = element.UIElement(
        center_position=(900, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="33",
        id="us33",
        action=None
    )
    country_us_34 = element.UIElement(
        center_position=(820, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="34",
        id="us34",
        action=None
    )
    country_us_35 = element.UIElement(
        center_position=(980, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="35",
        id="us35",
        action=None
    )
    country_us_36 = element.UIElement(
        center_position=(1035, 490),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="36",
        id="us36",
        action=None
    )
    country_us_37 = element.UIElement(
        center_position=(1035, 650),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text="37",
        id="us37",
        action=None
    )
    usmapimage = pygame.image.load("assets/USMAP.png")
    buttons = [country_us_1,country_us_2,country_us_3,
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
               country_us_34,country_us_35,country_us_36,
               country_us_37,return_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)
        screen.blit(usmapimage,(50,0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            #ossama el fucntion deh 3ashan 25ly text ely yzhr 3la map
            # id bta3ha 3ashan tb2a refrence lena f 23mlha zyha fy egp
            #wa b3den 23mlha comment
            #button.set_text(button.id)
            button.update_text(button.text,DARKBLUE)
            if ui_action is not None:
                return ui_action
            button.draw(screen)


        pygame.display.flip()
