import pygame
import os


class Lamp:
    def __init__(self, x, y, charge):
        self.lamp_on = pygame.image.load(os.path.join("game_assets", "lightbulb_on.png"))
        self.lamp_on = pygame.transform.scale(self.lamp_on, [50, 50])
        self.lamp_off = pygame.image.load(os.path.join("game_assets", "lightbulb_off.png"))
        self.lamp_off = pygame.transform.scale(self.lamp_off, [50, 50])
        self.pos = x, y
        self.charge = charge
        self.connected = []
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.lamp_rect = self.lamp_on.get_rect(center=(self.pos[0], self.pos[1]))

    def draw(self, win):
        """
        Draw a line
        :param win: Surface
        :return:
        """
        for line in self.connected:
            pygame.draw.aaline(win, (0, 0, 0), (self.pos[0], self.pos[1]), (line.pos[0], line.pos[1]))

    def draw_lamp(self, win, stock):
        """
        Draw a lamp and a charge of this lamp
        :param stock: is stock or not
        :param win: Surface
        :return:
        """
        self.lamp_rect = self.lamp_on.get_rect(center=(self.pos[0], self.pos[1]))
        win.blit(self.lamp_on, self.lamp_rect)
        if not stock:
            text = self.myfont.render(str(self.charge), False, (0, 0, 0))
            text_rect = text.get_rect(center=self.pos)
            win.blit(text, text_rect)

    def give(self):
        """

        :return: None
        """
        self.charge -= len(self.connected)
        for lamp in self.connected:
            lamp.charge += 1

    def take(self):
        """

        :return: None
        """
        self.charge += len(self.connected)
        for lamp in self.connected:
            lamp.charge -= 1
