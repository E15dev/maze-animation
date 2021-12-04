import pygame
import time
import random
import math


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
    pygame.draw.line(screen, (255, 0, 0), (center_width - xm - 5, center_height - ym - 5), (center_width - xm + 5, center_height - ym + 5))
    pygame.draw.line(screen, (255, 0, 0), (center_width - xm - 5, center_height - ym + 5), (center_width - xm + 5, center_height - ym - 5))


# config
cell_size = 25
xm = 0
ym = 0
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
    if iteration % 50 == 0:
        random.seed(time.time())
        xm -= ((random.randrange(0, 2) * 2) - 1) * cell_size
        ym -= ((random.randrange(0, 2) * 2) - 1) * cell_size
        # print(xm, ym)
        # xm += cell_size

print('end')
