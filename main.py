import pygame


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))

    def run(self):
        run = True

        while run:
            for event in pygame.event():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()


g = Game()
g.run()
