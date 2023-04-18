# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
RESOURCE_PATH = './resources/'

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.images = []

        img = pygame.image.load(RESOURCE_PATH + 'bud.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('test')
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    player = Player()
    bg = pygame.image.load(RESOURCE_PATH + 'background.png')
    SCREEN.fill(BLACK)
    pygame.display.flip()

    player.rect.x = 50  # go to x
    player.rect.y = 50  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            SCREEN.blit(bg, (0,0))
            pygame.display.update()
            player_list.draw(SCREEN)
            pygame.display.update()
            player.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                    player.control(-5, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                    player.control(5, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up')
                    player.control(0, 5)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down')
                    player.control(0, -5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                    player.control(5, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                    player.control(-5, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up stop')
                    player.control(0, -5)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down stop')
                    player.control(0, 5)
                if event.key == ord('q'):
                    is_running = False
        player.update()
        pygame.display.flip()
        clock.tick(30)


    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
