import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Tic Tac Toe')

    def menu():
        while True:

            screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def game():
        pass

    menu()