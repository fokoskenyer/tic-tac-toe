import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((610,610))
    pygame.display.set_caption('Tic Tac Toe')

    def menu():
        while True:

            screen.fill((0,0,0))

            tiles = {

                'top_left':pygame.Rect(0,0,200,200),
                'top_mid':pygame.Rect(205,0,200,200),
                'top_right':pygame.Rect(410,0,200,200),

                'mid_left':pygame.Rect(0,205,200,200),
                'mid_mid':pygame.Rect(205,205,200,200),
                'mid_right':pygame.Rect(410,205,200,200),

                'bot_left':pygame.Rect(0,410,200,200),
                'bot_mid':pygame.Rect(205,410,200,200),
                'bot_right':pygame.Rect(410,410,200,200)
            }

            pygame.draw.rect(screen,(255, 253, 208),tiles['top_left'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['top_mid'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['top_right'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['mid_left'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['mid_mid'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['mid_right'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['bot_left'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['bot_mid'])
            pygame.draw.rect(screen,(255, 253, 208),tiles['bot_right'])


            pos = pygame.mouse.get_pos()
            if tiles['bot_mid'].collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print("asd")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def game():
        pass

    menu()