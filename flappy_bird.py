import pygame
import neat
import time
import os
import random

WIND_WIDTH = 600
WIN_HEIGHT = 800


def create_surface(image_name) -> pygame.surface:
    image_path = os.path.join("imgs", image_name)
    img = pygame.image.load(image_path)
    return pygame.transform.scale2x(img)


BIRD_IMGS = [
    create_surface("bird1.png"),
    create_surface("bird2.png"),
    create_surface("bird3.png")
]

PIPE_IMG = create_surface('pipe.png')
BASE_IMG = create_surface('base.png')
BG_IMG = create_surface('bg.png')
