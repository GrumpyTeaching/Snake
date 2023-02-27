import pygame, sys
import random
from pygame.locals import *

SIZE = 10
WIDTH = 35
HEIGHT = 25

pygame.init()
size = (WIDTH * SIZE, HEIGHT * SIZE)
screen = pygame.display.set_mode(size)
background = (80, 80, 80)

def game_to_screen(x, y):
    return x * SIZE, y * SIZE

clock = pygame.time.Clock()

# from pygame.locals import *
# import random

def draw():
    screen.fill(background)
    x, y = food
    (screen_x, screen_y) = game_to_screen(x, y)
    color = (255, 100, 100)
    rect = ((screen_x, screen_y), (SIZE, SIZE))
    pygame.draw.rect(screen, color, rect)
    for part in snake:
        x, y = part
        (screen_x, screen_y) = game_to_screen(x, y)
        color = (0, 255, 0)
        rect = ((screen_x, screen_y), (SIZE, SIZE))
        pygame.draw.rect(screen, color, rect)
    pygame.display.update()
    
def new_food():
    global food
    x = random.randrange(SIZE)
    y = random.randrange(SIZE)
    food = (x, y)

def move():
    x, y = snake[0]
    dx, dy = step
    new_x = (x + dx + WIDTH) % WIDTH
    new_y = (y + dy + HEIGHT) % HEIGHT
    snake.insert(0, (new_x, new_y))
    global grow
    if grow == False:
        snake.pop()
    else:
        grow = False

def touch():
    global gameover
    for field in snake[1:]:
        if field == snake[0]:
            gameover = True

def eat():
    global grow
    if snake[0] == food:
        new_food()
        grow = True
        global speed
        speed = speed + 1
    
gameover = False
snake = [(22, 20), (21, 20), (20, 20), (19, 20), (18, 20)]
step = (1, 0)
speed = 1
grow = False
paused = False
new_food()

pygame.display.set_caption('Hello World!')
while not gameover:
    if not paused:
        move()
        eat()
        touch()
    draw()
    clock.tick(4 + speed)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                step = (0, -1)
            if event.key == K_LEFT:
                step = (-1, 0)
            if event.key == K_RIGHT:
                step = (1, 0)
            if event.key == K_DOWN:
                step = (0, 1)
            if event.key == K_SPACE:
                paused = True
        if event.type == KEYUP:
            if event.key == K_SPACE:
                paused = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
