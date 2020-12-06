import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIelement
from UIelement import *
import gamestate
from gamestate import GameState
import EGGame
from EGGame import *
import player
from player import *

import random

BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)


def egypt_screen(screen):
    element = UIelement
    c0 = Country("Return to main menu", "Return to main menu")
    element= UIelement


    c0=Country("Return to main menu","Return to main menu")
    c1 = Country(1, "eg1")
    c2 = Country(2, "eg2")
    c3 = Country(3, "eg3")
    c4 = Country(4, "eg4")
    c5 = Country(5, "eg5")
    c6 = Country(6, "eg6")
    c7 = Country(7, "eg7")
    c8 = Country(8, "eg8")
    c9 = Country(9, "eg9")
    c10 = Country(10, "eg10")
    c11 = Country(11, "eg11")
    c12 = Country(12, "eg12")
    c13 = Country(13, "eg13")
    c14 = Country(14, "eg14")
    c15 = Country(15, "eg15")
    c16 = Country(16, "eg16")
    c17 = Country(17, "eg17")
    c18 = Country(18, "eg18")
    c19 = Country(19, "eg19")
    c20 = Country(20, "eg20")
    c21 = Country(21, "eg21")
    c22 = Country(22, "eg22")
    

    c1.neighbors = {c2, c3, c7, c8}
    c2.neighbors = {c1, c3, c4, c19, c20, c21, c22}
    c3.neighbors = {c1, c2, c4, c5, c6, c7, c10, c13}
    c4.neighbors = {c2, c3, c5, c18, c19}
    c5.neighbors = {c3, c4, c6, c18}
    c6.neighbors = {c3, c5}
    c7.neighbors = {c1, c3, c8, c9, c10}
    c8.neighbors = {c1, c7}
    c9.neighbors = {c7, c10, c11}
    c10.neighbors = {c3, c7, c9, c11, c12, c13}
    c11.neighbors = {c9, c10, c12}
    c12.neighbors = {c10, c11, c13, c14, c15}
    c13.neighbors = {c3, c5, c10, c12, c15, c18}
    c14.neighbors = {c12, c15, c16}
    c15.neighbors = {c12, c13, c14, c16, c17, c18}
    c16.neighbors = {c14, c15, c17}
    c17.neighbors = {c15, c16}
    c18.neighbors = {c4, c5, c13, c15, c19, c20, c21, c22}
    c19.neighbors = {c2, c4, c18, c20}
    c20.neighbors = {c2, c18, c19, c21}
    c21.neighbors = {c2, c18, c20, c22}
    c22.neighbors = {c2, c18, c21}
    redPlayer = player(DARKRED)
    bluePlayer = player(DARKBLUE)
    available_countries = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                           c11, c12, c13, c14, c15, c16, c17, c18, c19,
                           c20, c21, c22]
    available_countriesIDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                              11, 12, 13, 14, 15, 16, 17, 18, 19,
                              20, 21, 22]
    redPlayer = player(DARKRED)
    bluePlayer = player(DARKBLUE)
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
                while country.troops == 3:
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
                while country.troops == 3:
                    country = random.choice(bluePlayer.countries)
                blueTroops -= 1
            country.increaseNumOfTroops(1)
            if blueTroops == 0:
                canAddBlue = False

    return_btn = element.UIElement(
        center_position=(150, 720),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        id="0",
        country=c0,
        action=GameState.TITLE,
    )

    country_eg_1 = element.UIElement(
        center_position=(240, 142),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c1.color,
        text=c1.label,
        country=c1,
        id="eg1",
        action=None
    )
    country_eg_2 = element.UIElement(
        center_position=(380, 530),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c2.color,
        text=c2.label,
        country=c2,
        id="eg2",
        action=None
    )
    country_eg_3 = element.UIElement(
        center_position=(485, 265),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c3.color,
        text=c3.label,
        country=c3,
        id="eg3",
        action=None
    )
    country_eg_4 = element.UIElement(
        center_position=(650, 268),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c4.color,
        text=c4.label,
        country=c4, id="eg4",
        action=None
    )
    country_eg_5 = element.UIElement(
        center_position=(626.5, 235),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=c5.color,
        text=c5.label,
        country=c5,
        id="eg5",
        action=None
    )
    country_eg_6 = element.UIElement(
        center_position=(677, 201),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=c6.color,
        text=c6.label,
        country=c6,
        id="eg6",
        action=None
    )
    country_eg_7 = element.UIElement(
        center_position=(650, 113),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c7.color,
        text=c7.label,
        country=c7, id="eg7",
        action=None
    )
    country_eg_8 = element.UIElement(
        center_position=(597, 101),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=c8.color,
        text=c8.label,
        country=c8,
        id="eg8",
        action=None
    )
    country_eg_9 = element.UIElement(
        center_position=(720, 65),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=c9.color,
        text=c9.label,
        country=c9,
        id="eg9",
        action=None
    )
    country_eg_10 = element.UIElement(
        center_position=(726, 114),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=c10.color,
        text=c10.label,
        country=c10,
        id="eg10",
        action=None
    )
    country_eg_11 = element.UIElement(
        center_position=(773, 81),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=c11.color,
        text=c11.label,
        country=c11,
        id="eg11",
        action=None
    )
    country_eg_12 = element.UIElement(
        center_position=(787, 117),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=c12.color,
        text=c12.label,
        country=c12,
        id="eg12",
        action=None
    )
    country_eg_13 = element.UIElement(
        center_position=(785, 177),
        font_size=35,
        bg_rgb=WHITE,
        text_rgb=c13.color,
        text=c13.label,
        country=c13,
        id="eg13",
        action=None
    )
    country_eg_14 = element.UIElement(
        center_position=(864, 112),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=c14.color,
        text=c14.label,
        country=c14,
        id="eg14",
        action=None
    )
    country_eg_15 = element.UIElement(
        center_position=(861, 178),
        font_size=40,
        bg_rgb=WHITE,
        text_rgb=c15.color,
        text=c15.label,
        country=c15,
        id="eg15",
        action=None
    )
    country_eg_16 = element.UIElement(
        center_position=(1011, 105),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c16.color,
        text=c16.label,
        country=c16,
        id="eg16",
        action=None
    )
    country_eg_17 = element.UIElement(
        center_position=(1011, 204),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c17.color,
        text=c17.label,
        country=c17,
        id="eg17",
        action=None
    )
    country_eg_18 = element.UIElement(
        center_position=(832, 325),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c18.color,
        text=c18.label,
        country=c18,
        id="eg18",
        action=None
    )
    country_eg_19 = element.UIElement(
        center_position=(735, 340),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=c19.color,
        text=c19.label,
        country=c19,
        id="eg19",
        action=None
    )
    country_eg_20 = element.UIElement(
        center_position=(800, 388),
        font_size=25,
        bg_rgb=WHITE,
        text_rgb=c20.color,
        text=c20.label,
        country=c20,
        id="eg20",
        action=None
    )
    country_eg_21 = element.UIElement(
        center_position=(910, 426),
        font_size=30,
        bg_rgb=WHITE,
        text_rgb=c21.color,
        text=c21.label,
        country=c21,
        id="eg21",
        action=None
    )
    country_eg_22 = element.UIElement(
        center_position=(918, 592),
        font_size=50,
        bg_rgb=WHITE,
        text_rgb=c22.color,
        text=c22.label,
        country=c22,
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
               country_eg_22, return_btn]
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
            button.update_text(button.country.label, button.country.color)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
