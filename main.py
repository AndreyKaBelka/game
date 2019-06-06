import pygame
import os
import Lamp


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))

    def run(self):
        clock = pygame.time.Clock()
        while 1:
            clock.tick(60)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit(0)
                if event.type == pygame.VIDEORESIZE:
                    self.width = event.w
                    self.height = event.h
                    self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)
                    self.bg = pygame.transform.scale(self.bg, [event.w, event.h])

                self.draw()

    def draw(self):
        self.win.blit(self.bg, [0, 0])

g = Game(1000, 700)
g.run()
