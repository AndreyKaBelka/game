import pygame


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode([self.width, self.height], flags=pygame.RESIZABLE)

    def run(self):
        while 1:
            self.win.fill([255, 255, 255])
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
                    self.win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


g = Game(1000, 700)
g.run()
