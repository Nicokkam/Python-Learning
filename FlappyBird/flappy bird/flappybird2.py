import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *

from BirdClass2 import *
from PipeClass2 import *
from Functions2 import *

import sqlite3
import time
import datetime

#==== Inicialization ==========================================================

FPS = 60
ANIMATION_SPEED = 0.18  # pixels per millisecond
WIN_WIDTH = 284 * 2     # BG image size: 284x512 px; agrupados 2x
WIN_HEIGHT = 512

pygame.init()
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pygame Flappy Bird')
clock = pygame.time.Clock()
score_font = pygame.font.SysFont(None, 32, bold=True)
images = load_images( )
intro = False

branco = (255,255,255)
iniciar = (0, 160, 255)
iniciarclaro = (0, 220, 255)
stop = (160, 0, 0)
stopclaro = (250, 0, 0)
preto = (0,0,0)

#==== Banco de dados ==========================================================
connection = sqlite3.connect('FlappyScore.db')
c = connection.cursor()

def create_tab():
    c.execute('create table if not exists dados (nome text, data text, pontos real)')
    
def dateentry(value):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H:%M:%S'))
    c.execute('insert into dados ( nome, data, pontos) values(?,?,?)',( "FlappyPlayer" , date, value)) #valores 

    connection.commit()
    
#==== Initial Screen ==========================================================
def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font, color, x, y):
    textSurface = font.render(text,True, color)
    algumRect = textSurface.get_rect()
    algumRect.center = (x,y)
    display_surface.blit(textSurface, algumRect)

def button(msg, x, y, w, h, ic, ac, action = None):
    """
    ic = Inative color
    ac  Active color
    MOUSE = Mouse Position
    CLICK = Mouse Clicks
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #Blink the button when mouse passes over
    if x + w > mouse[0] >x and y+h > mouse[1] > y:
        pygame.draw.rect(display_surface, ac, (x,y,w,h))
        #Click Function
        if click[0] == 1 and action != None:
           action() 
    else:
        pygame.draw.rect(display_surface, ic, (x,y,w,h))
   #Button Text     
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    text_objects(msg, smalltext, preto,(x+(w/2)),(y+(h/2)))

def intro():
    global intro
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                quitgame()
        for x in (0, WIN_WIDTH / 2):
            display_surface.blit(images['background'], (x, 0))
        font = pygame.font.Font('freesansbold.ttf', 60)
        text_objects("FlappyBird",font , branco, WIN_WIDTH/2, WIN_HEIGHT/4)
        button("Let's Flappy!",50,425,150,50,iniciar,iniciarclaro, main)
        button("QUIT!",400,425,100,50,stop,stopclaro, quitgame)
        pygame.display.flip()
    intro = False

#==== Main ====================================================================
def main():
 
    bird = Bird(50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2), 2,                       #Posicao inicial do bird. Nao se move em X
                (images['bird-wingup'], images['bird-wingdown']))
    
    pipes = deque() #Double Ended Que (Lista, pilha e fila). Usado como LISTA

    frame_clock = 0
    score = 0
    done = False
    
#------------------------------------------------------------------------------
    while not done:
        clock.tick(FPS)
        
        if not (frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):           #Acrescenta o tubo de acordo com o intervalo
            pp = PipePair(images['pipe-end'], images['pipe-body'])
            pipes.append(pp) #Adiciona na LISTA (deque)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break
            elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and
                    e.key in (K_UP, K_RETURN, K_SPACE)):
                bird.msec_to_climb = Bird.CLIMB_DURATION                        #O numero de ms restantes para a subida completa recebe a subida

#==== Main - Collisions =======================================================            
        pipe_collision = any(p.collides_with(bird) for p in pipes)
        """
        Any
        True: if at least one element of an iterable is true
        False: if all elements are false or if an iterable is empty
        """
        if pipe_collision or 0 >= bird.y or bird.y >= WIN_HEIGHT - Bird.HEIGHT: #SE bater nos tubos ou nas margens da tela
            done = True

#------------------------------------------------------------------------------
 
        for x in (0, WIN_WIDTH / 2):                                            #Constantemente coloca o background
            display_surface.blit(images['background'], (x, 0))

        while pipes and not pipes[0].visible:
            pipes.popleft()                                                     #Remove and retun an element from the left side of the deque

        for p in pipes:
            p.update()
            display_surface.blit(p.image, p.rect)

        bird.update()
        display_surface.blit(bird.image, bird.rect)
        
#==== Main - Update and Display Score =========================================           

        for p in pipes:
            if p.x + PipePair.WIDTH < bird.x and not p.score_counted:           #Nao ficar somando uma vez que passar
                score += 1
                p.score_counted = True
        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = WIN_WIDTH/2 - score_surface.get_width()/2                     #Posicionar no topo
        display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))   #Score também tem que se mover
        pygame.display.flip()
        frame_clock += 1
        
    print('Game over! Score: %i' % score)
    dateentry(score)  

#Main
create_tab()
intro()
main()
c.close()
connection.close()