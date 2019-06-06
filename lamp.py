import pygame
import os


class Lamp:
    def __init__(self, x, y, charge):
        self.lamp = pygame.image.load(os.path.join("game_assets", "lightbulb_on.png"))
        self.lamp = pygame.transform.scale(self.lamp, [50, 50])
        self.pos = x, y
        self.charge = charge
        self.connected = []
        '''
        for connect in connected:
            if not (connect == self.pos):
                self.connected.append(connect)
        '''
        self.lamp_rect = self.lamp.get_rect(center=(self.pos[0], self.pos[1]))

    def draw(self, win):
        """
        Draw a lamp
        :param win: Surface
        :return:
        """
        for line in self.connected:
            if line.pos != self.pos:
                pygame.draw.line(win, (0, 0, 0), (self.pos[0], self.pos[1]), (line.pos[0], line.pos[1]))

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
