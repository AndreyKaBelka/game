import pygame
import os
from lamp import Lamp
from random import randint


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.pos = [(361, 524), (875, 520), (639, 189), (500, 189)]
        self.lamps = []
        self.connected = [[1, 2, 3], [0, 2], [0, 1], [0]]

        for dot in self.pos:
            self.lamps.append(Lamp(dot[0], dot[1], randint(-3, 3)))
        count = 0
        for lampa in self.lamps:
            for i in range(len(self.connected[count])):
                lampa.connected.append(self.lamps[self.connected[count][i]])
            count += 1

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self):
        self.win.blit(self.bg, [0, 0])
        for la in self.lamps:
            la.draw(self.win)
        for la in self.lamps:
            if la.charge < 0:
                lamp = la.lamp_off
            else:
                lamp = la.lamp_on
            self.win.blit(lamp, la.lamp_rect)
            text = self.myfont.render(str(la.charge), False, (0, 0, 0))
            text_rect = text.get_rect(center=la.pos)
            self.win.blit(text, text_rect)

    def run(self):
        clock = pygame.time.Clock()
        run = True
        double_click_event = pygame.USEREVENT + 1
        timer = 0
        global timerset
        lamp = 0

        while run:
            clock.tick(60)
            pygame.display.update()
            gameover = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.VIDEORESIZE:
                    self.width = event.w
                    self.height = event.h
                    self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)
                    self.bg = pygame.transform.scale(self.bg, [event.w, event.h])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = (event.pos[0], event.pos[1])
                    global press
                    press = False
                    for la in self.lamps:
                        if la.lamp_rect.collidepoint(pos_mouse):
                            lamp = la
                            press = True
                            if timer == 0:
                                pygame.time.set_timer(double_click_event, 250)
                                timerset = True
                            elif timer == 1:
                                pygame.time.set_timer(double_click_event, 0)
                                # double click function
                                la.give()
                                timerset = False

                            if timerset:
                                timer = 1
                            else:
                                timer = 0

                elif event.type == double_click_event:
                    if press:
                        # single click
                        pygame.time.set_timer(double_click_event, 0)
                        timer = 0
                        lamp.take()

            self.draw()

            for charge in self.lamps:
                if charge.charge < 0:
                    gameover = False

            if gameover:
                run = False


if __name__ == "__main__":
    g = Game(1280, 720)
    g.run()
