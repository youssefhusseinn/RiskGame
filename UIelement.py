import pygame
import pygame.freetype
from pygame.sprite import Sprite
import USGame
from EGGame import EGGame
from USGame import *
import main
import math

from main import *
import USGame
from USGame import *
import Country
from Country import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255)
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)
def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb,id,country,action=None):

        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
        """
        self.country= country
        self.text=text
        self.font_size=font_size
        self.bg_rgb =bg_rgb
        self.text_rgb=text_rgb
        self.center_position= center_position
        self.id=id
        self.mouse_over = False  # indicates if the mouse is over the element
        #self.tet=text
        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()
        self.action = action


        # properties that vary the image and its rect when the mouse is over the element


    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
            return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos,mouse_up,c102,c101,redPlayer,bluePlayer):
            stateus =USGame()
            stateeg=EGGame()
            if self.rect.collidepoint(mouse_pos):
                self.mouse_over = True
                if mouse_up:
                    my_string = str(self.id)
                    if my_string.find("us") == False:
                        flag= stateus.addelements(self.country,c102,c101,redPlayer,bluePlayer)
                        if flag == True:
                            if(c101.label=="RED PLAYER"):
                                c101.label="BLUE PLAYER"
                                c101.color=bluePlayer.color
                                c101.setOwner(bluePlayer)
                                c102.setlabel(str (bluePlayer.bonustroops))
                                c102.color = bluePlayer.color
                                c102.setOwner(bluePlayer)
                                c102.setNumOfTroops(bluePlayer.bonustroops)
                                redPlayer.setbonustroops()
                                bluePlayer.setbonustroops()

                            else:
                                c101.label="RED PLAYER"
                                c101.color=redPlayer.color
                                c101.setOwner(redPlayer)
                                c102.setlabel(str(redPlayer.bonustroops))
                                c102.color = redPlayer.color
                                c102.setOwner(redPlayer)
                                c102.setNumOfTroops(redPlayer.bonustroops)
                                redPlayer.setbonustroops()
                                bluePlayer.setbonustroops()

                    if my_string.find("eg") == False:
                        flag= stateeg.addelements(self.country,c102,c101,redPlayer,bluePlayer)
                        if flag == True:
                            if(c101.label=="RED PLAYER"):
                                c101.label="BLUE PLAYER"
                                c101.color=bluePlayer.color
                                c101.setOwner(bluePlayer)


                            else:
                                c101.label="RED PLAYER"
                                c101.color=redPlayer.color
                                c101.setOwner(redPlayer)


                    return self.action
            else:
                self.mouse_over = False
    def update_bonus(self, mouse_pos,mouse_up,country,c102,c101,redPlayer,bluePlayer):
            stateus =USGame()
            stateeg=EGGame()
            if self.rect.collidepoint(mouse_pos):
                self.mouse_over = True
                if mouse_up:
                    my_string = str(self.id)
                    stateus.addbonustroops(self.country,c102,c101,redPlayer,bluePlayer)

                    return self.action
            else:
                self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)


    def set_text(self, text):
        default_image = create_surface_with_text(
            text=text, font_size=self.font_size, text_rgb=self.text_rgb, bg_rgb=self.bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=self.font_size* 1.2, text_rgb=self.text_rgb, bg_rgb=self.bg_rgb
        )

        # add both images and their rects to lists

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=self.center_position),
            highlighted_image.get_rect(center=self.center_position),
        ]
        self.text = text

    def update_text(self, text,text_rgb):
            default_image = create_surface_with_text(
                text=text, font_size=self.font_size, text_rgb=text_rgb, bg_rgb=self.bg_rgb
            )

            # create the image that shows when mouse is over the element
            highlighted_image = create_surface_with_text(
                text=text, font_size=self.font_size * 1.2, text_rgb=text_rgb, bg_rgb=self.bg_rgb
            )

            # add both images and their rects to lists

            self.images = [default_image, highlighted_image]
            self.rects = [
                default_image.get_rect(center=self.center_position),
                highlighted_image.get_rect(center=self.center_position),
            ]
            self.text = text

