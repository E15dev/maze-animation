import pygame
import time
import random
import math
from pynput.keyboard import *


def refresh():
    pygame.display.flip()
    return 0


def set_window_fps(fps):
    pygame.display.set_caption('pygame render ' + str(fps) + ' fps')


def get_state(x, y):
    random.seed((x * 0xFFFFFE) + y)
    x = random.randrange(0, 2)  # values for 0 to 1
    return bool(x)


def draw():
    for x in range(0, width + 100, cell_size):
        for y in range(0, height + 100, cell_size):
            if get_state(x + xm, y + ym):
                pygame.draw.line(screen, (255, 255, 255), (x, y), (x+cell_size, y+cell_size))
            else:
                pygame.draw.line(screen, (255, 255, 255), (x + cell_size, y), (x, y + cell_size))
    # draw map center
    pygame.draw.line(screen, (255, 0, 0), (center_width - xm - 5, center_height - ym - 5), (center_width - xm + 5, center_height - ym + 5))
    pygame.draw.line(screen, (255, 0, 0), (center_width - xm - 5, center_height - ym + 5), (center_width - xm + 5, center_height - ym - 5))


def press_on(key):
    global move_x, move_y
    key = str(key)
    if key == 'Key.left':
        move_x -= 1
    elif key == 'Key.up':
        move_y += 1
    elif key == 'Key.right':
        move_x += 1
    elif key == 'Key.down':
        move_y -= 1
    return 0


# config
cell_size = 25
xm = 0
ym = 0
move_x = 0
move_y = 0
(width, height) = (500, 500)  # screen resolution

# init
center_width = math.floor(width / 2)
center_height = math.floor(width / 2)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The game')
radius = 50
iteration = 0
frames_time = []

# more config
screen.fill((0, 0, 0))
pygame.display.flip()


with Listener(on_press = press_on) as listener:
    running = True
    while running:
        iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        try:
            fps = 1 / (time.time() - last_fps)
        except:
            fps = "error"
        set_window_fps(fps)
        last_fps = time.time()
        screen.fill((0, 0, 0))
        draw()
        refresh()  # swap buffer to screen
        xm -= move_x*cell_size
        move_x = 0
        ym += move_y*cell_size
        move_y = 0

print('end')
