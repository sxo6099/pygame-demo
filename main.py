# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
RESOURCE_PATH = './resources/'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('test')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    char = pygame.image.load(RESOURCE_PATH + 'bud.png')
    bg = pygame.image.load(RESOURCE_PATH + 'background.png')
    SCREEN.fill(BLACK)
    pygame.display.flip()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            SCREEN.blit(bg, (0,0))
            pygame.display.update()
            SCREEN.blit(char, (100, 100))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                if event.key == ord('q'):
                    is_running = False

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
