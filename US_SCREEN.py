import pygame
import pygame.freetype
import input_box
from PacifistAgent import PacifistAgent
from input_box import *
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
from PassiveAgent import *
from input_box import *
BLUE = (128, 128, 128)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)

def us_screen(screen,agent1,agent2):

    countriesPositions = [(200, 50),(150, 150), (100, 300), (270, 170), (195, 300),
                   (380, 100), (410, 220), (315, 310), (300, 460), (565, 110),
                    (565, 200),(565, 280), (450, 340),(430, 470), (600, 370),
                    (620, 450),(600, 580), (700, 170),(720, 270), (730, 380),
                    (770, 500),(750, 570), (800, 200),(900, 170), (800, 320),
                    (880, 310),(950, 310), (1050, 350), (1050, 270), (1100, 200),
                    (1050, 425), (900, 445), (900, 530), (820, 530), (980, 530),
                    (1035, 490), (1035, 650)]

    state= US_STATE(agent1, agent2)

    state.initializeState()
    element = UIElement
    inputbox = InputBox(1200, 100, 30, 40)
    input_boxes = [inputbox]
    return_btn = element.UIElement(
        center_position=(250, 700),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=BLACK,
        text="Return to main menu",
        id="0",
        action=GameState.TITLE
    )
    uiElements=[]

    element= UIElement
    turnLabel=element.UIElement(center_position=(1100,50),
                      font_size=30,
                      bg_rgb=WHITE,
                      text_rgb=BLACK,
                      text="red player",
                      action=5,
                      id=0,
                      )
    turnLabel_bonus=element.UIElement(center_position=(1250,50),
                      font_size=30,
                      bg_rgb=WHITE,
                      text_rgb=BLACK,
                      text="Bonus",
                      action=5,
                      id=0,
                      )
    GO_LABEL = element.UIElement(center_position=(1300, 200),
                                  font_size=30,
                                  bg_rgb=WHITE,
                                  text_rgb=(255,255,255),
                                  text="DO ATTACK",
                                  action=5,
                                  id=-1,
                                  )

    buttons=[turnLabel,turnLabel_bonus]
    i=0
    for country in countriesPositions:
        e=element.UIElement(center_position= countriesPositions[i],
                                            font_size=30,
                                            bg_rgb=WHITE,
                                            text_rgb=state.countries[i].owner.color,
                                            text=str(state.countries[i].numOfTroops,),
                                            action=5,
                                            id=i,
                                            )
        e.num="us"+str(i+1)
        uiElements.append(e)

        i+=1
    while True:

        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        screen.fill(BLUE)
        usmapimage = pygame.image.load("assets/USMAP.png")
        screen.blit(usmapimage, (50, 0))
        for event in pygame.event.get():
            text = inputbox.handle_event(event)
            if text != None:
              state.amountofattackingtroops=int(text)
            inputbox.update()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        for button in uiElements:
            addBonus=False
            button.update_text(str(state.countries[button.id].numOfTroops), state.countries[button.id].owner.color)
            if state.turn == False and state.agent1.bonusTroops > 0  :  # agent1 bonus adding turn
                addBonus=True
                arr2 = []
                for c in state.agent1.countries:
                    arr2.append(c.id)
                if button.num in arr2:
                    button.update_text(str(state.countries[button.id].numOfTroops) + '+',
                                       state.countries[button.id].owner.color)

            elif state.turn == True and state.agent2.bonusTroops > 0:  # agent1
                addBonus=True
                arr1 = []
                for c in state.agent2.countries:
                    arr1.append(c.id)
                if button.num in arr1:
                    button.update_text(str(state.countries[button.id].numOfTroops) + '+',
                                       state.countries[button.id].owner.color)
            ui_action1 = button.actionbutton(pygame.mouse.get_pos(), mouse_up, state, state.countries[button.id],addBonus)

            if ui_action1 is not None:

                return ui_action1
            button.draw(screen)

        ui_action2 = turnLabel.update(pygame.mouse.get_pos(), mouse_up)
        ui_action5= turnLabel_bonus.update(pygame.mouse.get_pos(), mouse_up)

        if state.turn == False:
            turnLabel.update_text("RED PLAYER : ", DARKRED)
            turnLabel_bonus.update_text(str(state.agent1.bonusTroops),DARKRED)
        else:
            turnLabel.update_text("BLUE PLAYER : ", DARKBLUE)
            turnLabel_bonus.update_text(str(state.agent2.bonusTroops), DARKBLUE)
        if ui_action5 is not None:
            return ui_action5
        if ui_action2 is not None:
            return ui_action2
        ui_action3 = return_btn.restart(pygame.mouse.get_pos(), mouse_up,state)
        if ui_action3 is not None:
            return ui_action3
        ui_action4 = GO_LABEL.updateAI(pygame.mouse.get_pos(), mouse_up,state)
        if ui_action4 is not None:
            return ui_action4
        turnLabel.draw(screen)
        turnLabel_bonus.draw(screen)
        return_btn.draw(screen)

        if (not state.turn and state.agent1.type != "HUMAN") or (state.turn and state.agent2.type != "HUMAN"):
            GO_LABEL.draw(screen)
        else:
            inputbox.draw(screen)

        MANUAL_CURSOR = pygame.image.load('assets/mouse.png').convert_alpha()
        screen.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))
        pygame.display.flip()


