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
import player
from player import *

BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)


def assignTroopsRandomly(redPlayer, bluePlayer, countries):
    available_countries = countries
    for i in range(0, 37, 1):
        country = random(available_countries)


def us_screen(screen):

    element = UIelement
    state = USGame()
    c100 = Country("TURN:", "TURN:")
    c101=Country("RED PLAYER","RED PLAYER")

    c0 = Country("Return to main menu", "Return to main menu")
    c1 = Country("us1", "us1")
    c2 = Country("us2", "us2")
    c3 = Country("us3", "us3")
    c4 = Country("us4", "us4")
    c5 = Country("us5", "us5")
    c6 = Country("us6", "us6")
    c7 = Country("us7", "us7")
    c8 = Country("us8", "us8")
    c9 = Country("us9", "us9")
    c10 = Country("us10", "us10")
    c11 = Country("us11", "us11")
    c12 = Country("us12", "us12")
    c13 = Country("us13", "us13")
    c14 = Country("us14", "us14")
    c15 = Country("us15", "us15")
    c16 = Country("us16", "us16")
    c17 = Country("us17", "us17")
    c18 = Country("us18", "us18")
    c19 = Country("us19", "us19")
    c20 = Country("us20", "us20")
    c21 = Country("us21", "us21")
    c22 = Country("us22", "us22")
    c23 = Country("us23", "us23")
    c24 = Country("us24", "us24")
    c25 = Country("us25", "us25")
    c26 = Country("us26", "us26")
    c27 = Country("us27", "us27")
    c28 = Country("us28", "us28")
    c29 = Country("us29", "us29")
    c30 = Country("us30", "us30")
    c31 = Country("us31", "us31")
    c32 = Country("us32", "us32")
    c33 = Country("us33", "us33")
    c34 = Country("us34", "us34")
    c35 = Country("us35", "us35")
    c36 = Country("us36", "us36")
    c37 = Country("us37", "us37")
    c0.neighbors = {}
    c1.neighbors = {c2, c4}
    c2.neighbors = {c1, c3, c4, c5}
    c3.neighbors = {c2, c5, c9}
    c4.neighbors = {c1, c2, c5, c6, c7, c8}
    c5.neighbors = {c2, c3, c4, c8, c9}
    c6.neighbors = {c4, c7, c10, c11}
    c7.neighbors = {c4, c6, c8, c11, c12, c13}
    c8.neighbors = {c4, c5, c7, c9, c13, c14}
    c9.neighbors = {c3, c5, c8, c13, c14}
    c10.neighbors = {c6, c11, c18}
    c11.neighbors = {c6, c7, c10, c12, c18, c19}
    c12.neighbors = {c7, c11, c13, c15, c19, c20}
    c13.neighbors = {c7, c8, c9, c12, c14, c15, c16}
    c14.neighbors = {c8, c9, c13, c16, c17}
    c15.neighbors = {c12, c13, c16, c20}
    c16.neighbors = {c13, c14, c15, c17, c20, c21}
    c17.neighbors = {c14, c16, c21, c22}
    c18.neighbors = {c10, c11, c19, c23, c24}
    c19.neighbors = {c11, c12, c18, c20, c23, c25}
    c20.neighbors = {c12, c15, c16, c19, c21, c25, c28, c32}
    c21.neighbors = {c16, c17, c20, c22, c32, c34}
    c22.neighbors = {c17, c21, c34}
    c23.neighbors = {c18, c19, c24, c25}
    c24.neighbors = {c23, c25, c26, c27}
    c25.neighbors = {c19, c20, c23, c26, c28}
    c26.neighbors = {c24, c25, c27, c28}
    c27.neighbors = {c24, c26, c28, c29}
    c28.neighbors = {c20, c25, c26, c27, c29, c31, c32}
    c29.neighbors = {c27, c28, c30}
    c30.neighbors = {c29}
    c31.neighbors = {c28, c32, c35, c36}
    c32.neighbors = {c20, c21, c28, c31, c33, c34, c35}
    c33.neighbors = {c32, c34, c35, c37}
    c34.neighbors = {c21, c22, c32, c33}
    c35.neighbors = {c31, c32, c36, c37}
    c36.neighbors = {c31, c35}
    c37.neighbors = {c33, c35}

    available_countries = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                           c11, c12, c13, c14, c15, c16, c17, c18, c19,
                           c20, c21, c22, c23, c24, c25, c26, c27, c28, c29,
                           c30, c31, c32, c33, c34, c35, c36, c37]
    redPlayer = player(DARKRED,"RED PLAYER")
    bluePlayer = player(DARKBLUE,"BLUE PLAYER")
    c101.setOwner(redPlayer)
    c101.color=redPlayer.color

    redTroops = 20
    blueTroops = 20

    canAddRed = True
    canAddBlue = True

    while canAddRed or canAddBlue:
        # redTroops
        if canAddRed:
            if available_countries.__len__() != 0:
                country = random.choice(available_countries)
                available_countries.remove(country)
                country.setOwner(redPlayer)
                redPlayer.addcountry(country)
                redTroops -= 1
            else:
                country = random.choice(redPlayer.countries)
                redTroops -= 1
            country.increaseNumOfTroops(1)
            if redTroops == 0:
                canAddRed = False
        # blueTroops
        if canAddBlue:

            if available_countries.__len__() != 0:
                country = random.choice(available_countries)
                available_countries.remove(country)
                country.setOwner(bluePlayer)
                bluePlayer.addcountry(country)
                blueTroops -= 1
            else:
                country = random.choice(bluePlayer.countries)
                blueTroops -= 1
            country.increaseNumOfTroops(1)
            if blueTroops == 0:
                canAddBlue = False

    return_btn = element.UIElement(
        center_position=(250, 700),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=BLACK,
        text="Return to main menu",
        id="0",
        country=c0,
        action=GameState.TITLE

    )

    country_us_1 = element.UIElement(
        center_position=(200, 50),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c1.color,
        text=c1.label,
        id="us1",
        country=c1,
        action=None
    )
    country_us_2 = element.UIElement(
        center_position=(150, 150),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c2.color,
        text=c2.label,
        id="us2",
        country=c2,
        action=None
    )
    country_us_3 = element.UIElement(
        center_position=(100, 300),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c3.color,
        text=c3.label,
        country=c3,
        id="us3",
        action=None

    )
    country_us_4 = element.UIElement(
        center_position=(270, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c4.color,
        text=c4.label,
        country=c4,
        id="us4",
        action=None
    )
    country_us_5 = element.UIElement(
        center_position=(195, 300),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c5.color,
        text=c5.label,
        country=c5,
        id="us5",
        action=None
    )
    country_us_6 = element.UIElement(
        center_position=(380, 100),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c6.color,
        text=c6.label,
        country=c6,
        id="us6",
        action=None
    )
    country_us_7 = element.UIElement(
        center_position=(410, 220),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=BLACK,
        text=c7.label,
        country=c7,
        id="us7",
        action=None
    )
    country_us_8 = element.UIElement(
        center_position=(315, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c8.color,
        text=c8.label,
        country=c8,
        id="us8",
        action=None
    )
    country_us_9 = element.UIElement(
        center_position=(300, 460),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c9.color,
        text=c9.label,
        country=c9,
        id="us9",
        action=None
    )
    country_us_10 = element.UIElement(
        center_position=(565, 110),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c10.color,
        text=c10.label,
        country=c10,
        id="us10",
        action=None
    )
    country_us_11 = element.UIElement(
        center_position=(565, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c11.color,
        text=c11.label,
        country=c11,
        id="us11",
        action=None
    )
    country_us_12 = element.UIElement(
        center_position=(565, 280),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c12.color,
        text=c12.label,
        country=c12,
        id="us12",
        action=None
    )
    country_us_13 = element.UIElement(
        center_position=(450, 340),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c13.color,
        text=c13.label,
        country=c13,
        id="us13",
        action=None
    )
    country_us_14 = element.UIElement(
        center_position=(430, 470),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c14.color,
        text=c14.label,
        country=c14,
        id="us14",
        action=None
    )
    country_us_15 = element.UIElement(
        center_position=(600, 370),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c15.color,
        text=c15.label,
        country=c15,
        id="us15",
        action=None
    )
    country_us_16 = element.UIElement(
        center_position=(620, 450),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c16.color,
        text=c16.label,
        country=c16,
        id="us16",
        action=None
    )
    country_us_17 = element.UIElement(
        center_position=(600, 580),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c17.color,
        text=c17.label,
        country=c17,
        id="us17",
        action=None
    )
    country_us_18 = element.UIElement(
        center_position=(700, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c18.color,
        text=c18.label,
        country=c18,
        id="us18",
        action=None
    )
    country_us_19 = element.UIElement(
        center_position=(720, 270),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c19.color,
        text=c19.label,
        country=c19,
        id="us19",
        action=None
    )
    country_us_20 = element.UIElement(
        center_position=(730, 380),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c20.color,
        text=c20.label,
        country=c20,
        id="us20",
        action=None
    )
    country_us_21 = element.UIElement(
        center_position=(750, 480),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c21.color,
        text=c21.label,
        country=c21, id="us21",
        action=None
    )
    country_us_22 = element.UIElement(
        center_position=(750, 570),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c22.color,
        text=c22.label,
        country=c22, id="us22",
        action=None
    )

    country_us_23 = element.UIElement(
        center_position=(800, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c23.color,
        text=c23.label,
        country=c23, id="us23",
        action=None
    )
    country_us_24 = element.UIElement(
        center_position=(900, 170),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c24.color,
        text=c24.label,
        country=c24,
        id="us24",
        action=None
    )
    country_us_25 = element.UIElement(
        center_position=(800, 320),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c25.color,
        text=c25.label,
        country=c25,
        id="us25",
        action=None
    )
    country_us_26 = element.UIElement(
        center_position=(880, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c26.color,
        text=c26.label,
        country=c26,
        id="us26",
        action=None
    )
    country_us_27 = element.UIElement(
        center_position=(950, 310),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c27.color,
        text=c27.label,
        country=c27,
        id="us27",
        action=None
    )
    country_us_28 = element.UIElement(
        center_position=(1050, 350),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c28.color,
        text=c28.label,
        country=c28,
        id="us28",
        action=None
    )
    country_us_29 = element.UIElement(
        center_position=(1050, 270),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c29.color,
        text=c29.label,
        country=c29,
        id="us29",
        action=None
    )
    country_us_30 = element.UIElement(
        center_position=(1100, 200),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c30.color,
        text=c30.label,
        country=c30,
        id="us30",
        action=None
    )
    country_us_31 = element.UIElement(
        center_position=(1050, 425),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c31.color,
        text=c31.label,
        country=c31,
        id="us31",
        action=None
    )
    country_us_32 = element.UIElement(
        center_position=(900, 445),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c32.color,
        text=c32.label,
        country=c32,
        id="us32",
        action=None
    )
    country_us_33 = element.UIElement(
        center_position=(900, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c33.color,
        text=c33.label,
        country=c33,
        id="us33",
        action=None
    )
    country_us_34 = element.UIElement(
        center_position=(820, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c34.color,
        text=c34.label,
        country=c34,
        id="us34",
        action=None
    )
    country_us_35 = element.UIElement(
        center_position=(980, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c35.color,
        text=c35.label,
        country=c35,
        id="us35",
        action=None
    )
    country_us_36 = element.UIElement(
        center_position=(1035, 490),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c36.color,
        text=c36.label,
        country=c36,
        id="us36",
        action=None
    )
    country_us_37 = element.UIElement(
        center_position=(1035, 650),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c37.color,
        text=c37.label,
        country=c37,
        id="us37",
        action=None
    )
    turn_button = element.UIElement(
        center_position=(1150, 50),
        font_size=20,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text="TURN :",
        country=c100,
        id="turnid",
        action=None
    )
    player_button = element.UIElement(
        center_position=(1260, 50),
        font_size=20,
        bg_rgb=WHITE,
        text_rgb=WHITE,
        text="TURN :",
        country=c101,
        id="playerid",
        action=None
    )
    usmapimage = pygame.image.load("assets/USMAP.png")
    buttons = [country_us_1, country_us_2, country_us_3,
               country_us_4, country_us_5, country_us_6,
               country_us_7, country_us_8, country_us_9,
               country_us_10, country_us_11, country_us_12,
               country_us_13, country_us_14, country_us_15,
               country_us_16, country_us_17, country_us_18,
               country_us_19, country_us_20, country_us_21,
               country_us_22, country_us_23, country_us_24,
               country_us_25, country_us_26, country_us_27,
               country_us_28, country_us_29, country_us_30,
               country_us_31, country_us_32, country_us_33,
               country_us_34, country_us_35, country_us_36,
               country_us_37, return_btn,turn_button,player_button]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)
        screen.blit(usmapimage, (50, 0))
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up,c101,redPlayer,bluePlayer)
            button.update_text(button.country.label, button.country.color)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        pygame.display.flip()
