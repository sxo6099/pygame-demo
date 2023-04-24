# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

import Enemy
import Player
import Projectile

RESOURCE_PATH = './resources/'

WIDTH = 1920
HEIGHT = 1080

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pygame.init()
    pygame.mixer.music.load(RESOURCE_PATH + '01 - Overture.mp3')
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('test')
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    player = Player.player()
    blob = Projectile.projectile()
    orc = Enemy.orc()
    bg = pygame.image.load(RESOURCE_PATH + 'background.png')
    SCREEN.fill(BLACK)
    pygame.display.flip()

    player.rect.x = 50  # go to x
    player.rect.y = 50  # go to y
    orc.rect.x = WIDTH - 500
    orc.rect.y = HEIGHT - 500
    player_list = pygame.sprite.Group()
    player_list.add(player)
    player_list.add(blob)
    player_list.add(orc)

    is_running = True
    pygame.mixer.music.set_volume(.02)
    pygame.mixer.music.play()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            SCREEN.blit(bg, (0,0))
            pygame.display.update()
            player_list.draw(SCREEN)
            pygame.display.update()
            player.update()
            if pygame.sprite.collide_rect(orc, blob):
                orc.kill()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                    player.control(-5, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                    player.control(5, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up')
                    player.control(0, -5) #flipped because array of pixels?
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down')
                    player.control(0, 5)
                if event.key == pygame.K_SPACE:
                    print('space')
                    blob.control(player.rect.x, player.rect.y)
                    blob.update()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                    player.control(5, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                    player.control(-5, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('up stop')
                    player.control(0, 5)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down stop')
                    player.control(0, -5)
                if event.key == ord('q'):
                    is_running = False
        player.update()
        orc.update()
        pygame.display.flip()
        clock.tick(30)


    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
