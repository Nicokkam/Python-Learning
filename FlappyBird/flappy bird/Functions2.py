import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *

from BirdClass2 import *




FPS = 60
ANIMATION_SPEED = 0.18  # pixels per millisecond
WIN_WIDTH = 284 * 2     # BG image size: 284x512 px; tiled twice
WIN_HEIGHT = 512




def load_images():
    """Carrega todas as imagens e retorna um dicionário
    """

    def load_image(img_file_name):
        """Retorna a imagem que foi carregada no pygame com o nome especificado 
        As imagens estao na mesma pasta do programa
        Todas as imagens sao convertidas

        Argumentos:
        img_file_name: Nome do arquivo
        """
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background.png'),
            'pipe-end': load_image('pipe_end.png'),
            'pipe-body': load_image('pipe_body.png'),
            'bird-wingup': load_image('bird_wing_up.png'),
            'bird-wingdown': load_image('bird_wing_down.png')}

 
def frames_to_msec(frames, fps=FPS):
    """Converte os Frames para milisegundos com o framerate especificado

    Argumentos:
    frames: Quantos frames para converter para ms
    fps: A taxa de frame para converter.  Padrao: FPS.
    """
    return 1000.0 * frames / fps


def msec_to_frames(milliseconds, fps=FPS):
    """Converte milisegundos para frames com o framerate especificado.

    Argumentos:
    milliseconds: Quantos ms para converter para frames.
    fps: A taxa de frame para converter.  Padrao: FPS.
    """
    return fps * milliseconds / 1000.0


