import pygame
import pygame.freetype
from pygame.sprite import Sprite
import UIElement
from UIElement import *
import main
from main import *

BLUE = (9, 5, 101)
WHITE = (255, 255, 255)


class UISprite(pygame.sprite.Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self,center_position,strnormal,strbig,):
        self.mouse_over =True  # indicates if the mouse is over the element
        self.defaultimage = pygame.image.load(strnormal)
        self.bigimage = pygame.image.load(strbig)
        self.images = [self.defaultimage,self.bigimage]
        self.rects = [
            self.defaultimage.get_rect(center=center_position),
            self.bigimage.get_rect(center=center_position),
        ]
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
