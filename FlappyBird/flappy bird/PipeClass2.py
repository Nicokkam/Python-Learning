import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *

from BirdClass2 import *

#==== Inicialization ==========================================================
FPS = 60
ANIMATION_SPEED = 0.18  # pixels per millisecond
WIN_WIDTH = 284 * 2     # BG image size: 284x512 px; tiled twice
WIN_HEIGHT = 512

#==== Definitions =============================================================
def frames_to_msec(frames, fps=FPS):
    return 1000.0 * frames / fps

#==== Class ===================================================================
class PipePair(pygame.sprite.Sprite):
    """
    Parte de cima e de baixo do tubo

    Attributos:
    x: Posicao em X. Float. Y sempre 0!
        
    mask: Colisao
    
    top_pieces: The number of pieces, including the end piece, in the
        top pipe.
    bottom_pieces: The number of pieces, including the end piece, in
        the bottom pipe.

    Constantes:
    WIDTH: Largura, em pixels do tubo. (Mesma largura da imagem)
    PIECE_HEIGHT: Altura do tubo
    ADD_INTERVAL: Intervalo, em ms, entre um tubo e o outro.
    """

    WIDTH = 80
    PIECE_HEIGHT = 32
    ADD_INTERVAL = 1500

    def __init__(self, pipe_end_img, pipe_body_img):
        """Gera um tubo aleatório

        Gerará um pipe aleatorio em x de float(WIN_WIDTH - 1), ou seja. final da tela.

        Argumentos:
        pipe_end_img: Imagem de fim do tubo
        pipe_body_img: Imagem do corpo do tubo
        """
        self.x = float(WIN_WIDTH - 1)
        self.score_counted = False
        self.image = pygame.Surface((PipePair.WIDTH, WIN_HEIGHT), SRCALPHA) #Surface((width, height), masks=None)
        self.image.convert()   # speeds up blitting
        self.image.fill((0, 0, 0, 0))
        total_pipe_body_pieces = int(      #Gerando um número inteiro que preencha a tela com essas informacoes
            (WIN_HEIGHT -                  # Preenche a tela do topo ao bottom
             3 * Bird.HEIGHT -             # Espaco para caber o bird
             3 * PipePair.PIECE_HEIGHT) /  # 2 fim de tubo + 1 corpo do tubo (3 pieces)
            PipePair.PIECE_HEIGHT          # Numero de pedacos do tubo
        )
        self.bottom_pieces = randint(1, total_pipe_body_pieces) #Numero aleatorio entre 1 e o total de pedacos (bottom)
        self.top_pieces = total_pipe_body_pieces - self.bottom_pieces #O restante para completar (top)

        #Exemplo da parte acima
        """
         total_pipe_body_pieces = int((512 - 3*50 - 3*32)/32) #Resultado é 8
         self.bottom_pieces = 5
         self.top_pieces = 3
         
         Mesmo exemplo aplicado nas contas abaixo
         """

        # bottom pipe
        for i in range(1, self.bottom_pieces + 1):                              #De 1 até 6
            piece_pos = (0, WIN_HEIGHT - i*PipePair.PIECE_HEIGHT)               #32 pixels, 64, 96...
            self.image.blit(pipe_body_img, piece_pos)                           #Colocar um pipe body
        bottom_pipe_end_y = WIN_HEIGHT - self.bottom_height_px                  #Altura total do bottom pipe
        bottom_end_piece_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)   #Posicao do END PIPE
        self.image.blit(pipe_end_img, bottom_end_piece_pos)                     #Colocar o END PIPE 

        # top pipe
        for i in range(self.top_pieces):
            self.image.blit(pipe_body_img, (0, i * PipePair.PIECE_HEIGHT))
        top_pipe_end_y = self.top_height_px
        self.image.blit(pipe_end_img, (0, top_pipe_end_y))

        # compensate for added end pieces
        self.top_pieces += 1
        self.bottom_pieces += 1

        # for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def top_height_px(self):
        """Altura do TOP pipe em pixels"""
        return self.top_pieces * PipePair.PIECE_HEIGHT

    @property
    def bottom_height_px(self):
        """Altura do BOTTOM pipe em pixels"""
        return self.bottom_pieces * PipePair.PIECE_HEIGHT

    @property
    def visible(self):
        """Retorna se o pipe está visivel na tela ou nope"""
        return -PipePair.WIDTH < self.x < WIN_WIDTH

    @property
    def rect(self):
        """Cria o Rect que representa o pipe"""
        return Rect(self.x, 0, PipePair.WIDTH, PipePair.PIECE_HEIGHT)

    def update(self, delta_frames=1):
        """Atualiza a posicao

        Argumentos:
        delta_frames: Numero de frames decorridos desde que este metodo foi chamado
        """
        self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)

    def collides_with(self, bird):
        """Se o bird collide com o pipe
        
        Argumentos:
        bird: O bird que deve ser testado com a colisao
        """
        return pygame.sprite.collide_mask(self, bird)