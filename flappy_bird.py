from typing import List, Union

import pygame
import neat
import time
import os
import random

from pygame import Surface
from pygame.surface import SurfaceType

WIND_WIDTH = 600
WIN_HEIGHT = 800


def create_surface(image_name) -> pygame.surface:
    image_path = os.path.join("imgs", image_name)
    img = pygame.image.load(image_path)
    return pygame.transform.scale2x(img)


BIRD_IMGES = [
    create_surface("bird1.png"),
    create_surface("bird2.png"),
    create_surface("bird3.png")
]

PIPE_IMG = create_surface('pipe.png')
BASE_IMG = create_surface('base.png')
BG_IMG = create_surface('bg.png')

class Bird:
    IMAGES = BIRD_IMGES
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATIONAL_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img = self.IMAGES[0]