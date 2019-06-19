import pygame
import os
from lamp import Lamp


class Construct:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.pos = []
        self.lamps = []
        self.stock = Lamp(25, self.height - 25, 1)
        self.press = False
        self.connected = []
        pygame.font.init()
        self.draw_line = False
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.connect = []
        self.mouse_pos = []

    def draw(self, mouse_pose):
        self.win.blit(self.bg, [0, 0])
        self.stock.draw_lamp(self.win)
        if mouse_pose:
            pygame.draw.aaline(self.win, (0, 0, 0), pos_line, mouse_pose)
            print("sosi")
        for la in self.lamps:
            la.draw(self.win)
        for la in self.lamps:
            la.draw_lamp(self.win)
        pygame.draw.rect(self.win, (255, 255, 255), (self.width - 155, 0, 150, 40))
        text = self.myfont.render("Сохранить", False, (0, 0, 0))
        self.win.blit(text, (self.width - 155, 0))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.VIDEORESIZE:
                    self.width = event.w
                    self.height = event.h
                    self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)
                    self.bg = pygame.transform.scale(self.bg, [event.w, event.h])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = (event.pos[0], event.pos[1])
                    global lamp
                    global connected_lamp
                    if event.button == 1:
                        if self.stock.lamp_rect.collidepoint(pos_mouse):
                            self.press = True
                            self.lamps.append(Lamp(pos_mouse[0], pos_mouse[1], 0))
                            lamp = self.lamps[len(self.lamps) - 1]
                        for la in self.lamps:
                            if la.lamp_rect.collidepoint(pos_mouse):
                                self.press = True
                                lamp = la
                        if self.width - 155 < event.pos[0] < self.width:
                            if 0 < event.pos[1] < 40:
                                pass

                    if event.button == 3:
                        self.draw_line = True
                        global pos_line
                        for i in range(len(self.lamps)):
                            la = self.lamps[i]
                            if la.lamp_rect.collidepoint(pos_mouse):
                                connected_lamp = i
                                pos_line = self.lamps[i].pos
                if event.type == pygame.MOUSEBUTTONUP:
                    self.press = False
                    self.mouse_pos = []
                    if self.draw_line:
                        pos_mouse = (event.pos[0], event.pos[1])
                        for i in range(len(self.lamps)):
                            la = self.lamps[i]
                            if la.lamp_rect.collidepoint(pos_mouse) and not (i == connected_lamp):
                                if la in self.lamps[connected_lamp].connected:
                                    pass
                                else:
                                    self.lamps[connected_lamp].connected.append(la)
                                    la.connected.append(self.lamps[connected_lamp])
                    self.draw_line = False
                if event.type == pygame.MOUSEMOTION and (self.press or self.draw_line):
                    if self.press:
                        lamp.pos = pygame.mouse.get_pos()
                    elif self.draw_line:
                        self.mouse_pos = pygame.mouse.get_pos()
            self.draw(self.mouse_pos)


if __name__ == "__main__":
    game = Construct(1200, 700)
    game.run()
