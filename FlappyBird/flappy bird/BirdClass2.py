import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *




FPS = 60
ANIMATION_SPEED = 0.18  # pixels per millisecond
WIN_WIDTH = 284 * 2     # BG image size: 284x512 px; tiled twice
WIN_HEIGHT = 512




def frames_to_msec(frames, fps=FPS):
    return 1000.0 * frames / fps



 
class Bird(pygame.sprite.Sprite):
    """Parametro representa que o jogador controla esta classe

    Attributos:
    x: Coordenada X do bird
    y: Coordenada Y do bird
    msec_to_climb: O numero de ms restantes para a subida completa. 
                    Uma subida completa é igual a Bird.CLIMB_DURATION milisegundos

    Constantes:
    WIDTH: 
    HEIGHT: 
    SINK_SPEED: Em qual velocidade, em pixels por ms, o bird cai 
                    em um segundo enquanto nao esta subindo 
    CLIMB_SPEED: Em qual velocidade, em pixels por ms, o bird sobe
                    em um segundo em média.
                    Ver também Bird.update docstring.
        
    CLIMB_DURATION: Numero de ms que o bird demora para executar uma subida completa
    """

    WIDTH = HEIGHT = 50 
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.5
    CLIMB_DURATION = 200

    def __init__(self, x, y, msec_to_climb, images):
        """
        x: Coordenada inicial em x.
        y: Coordenada inicial em Y.
        msec_to_climb: Se quiser que o bird de uma subida inicial
        images: Usar nesta ordem:
                0. Wings Up
                1. Wings Down
        """
        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup) #Mask para a colisao
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown) #Mask para a colisao

    def update(self, delta_frames=1):
        """Atualiza position. 
        
        Peguei a Física do bird na net :) (Linha 78, 79 e 80)

        Argumentos:
        delta_frames: Numero de frames decorridos desde que este metodo foi chamado
            
        """
        if self.msec_to_climb > 0: #Se o passaro esta subindo
            frac_climb_done = 1 - self.msec_to_climb/Bird.CLIMB_DURATION 
            self.y -= (Bird.CLIMB_SPEED * frames_to_msec(delta_frames) * 
                       (1 - math.cos(frac_climb_done * math.pi)))
            self.msec_to_climb -= frames_to_msec(delta_frames) #Vai tirando até ele chegar no topo
        else:
            self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames) #Se chegou no topo, cair

    @property
    def image(self):
        """Animacao do bird (asinhas)
        """
        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup
        else:
            return self._img_wingdown

    @property
    def mask(self):
        '''A mask serve para retirar a sobra do retangulo para os pixels da sprite 
            com transparencia maior que 127 em caso de colisao
	    '''
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

    @property
    def rect(self):
        """Bird position, largura, altura, como um pygame.Rect 
        """
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)