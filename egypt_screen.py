import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIelement
from UIelement import *
import gamestate
from gamestate import GameState
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)



def egypt_screen(screen):
    element= UIelement
    return_btn = element.UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    buttons=[return_btn]
    image = pygame.image.load(r'F:\risk\assets\egyptmap.png')




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
        screen.blit(image,(75,100))


        pygame.display.flip()