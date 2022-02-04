#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:46:48 2018

@author: NicolasK
"""

import sqlite3
import time
import datetime


connection = sqlite3.connect('FlappyScore.db')
c = connection.cursor()

#==============================================================================
# #SQL
#==============================================================================

def create_tab():
    c.execute('create table if not exists dados (nome text, data text, pontos real)')

def data_now():
   data = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d-%m-%Y %H:%M'))    
   return data  
    

def dateentry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H:%M:%S'))
    value = 0
    
#==============================================================================
#     cria o bd novo    
#    c.execute("insert into dados values (2,'###','###',0)")
#                           OU
#    c.execute('insert into dados (id, nome, date, value) values(?,?,?,?)', )
#                   (id, nome, data, value) #valores 
#==============================================================================
    c.execute('insert into dados ( nome, data, pontos) values(?,?,?)',( "Player 1" , date, value)) #valores 
   # c.execute('insert into dados ( nome, data, pontos) values(?,?,?)',( "Player 2" , date, value))    
    #c.execute("insert into dados values (1,'Player 1', (?),0)")    
    #c.execute("insert into dados values (2,'Player 2',(?),0)", )
#==============================================================================
# salva o bd
#==============================================================================
    connection.commit()       

def atualizar(winer):
#==============================================================================
#     seleciona os pontos do jogador passado por parametro
#==============================================================================
    c.execute("SELECT pontos FROM dados WHERE nome = '" + winer + "'")
    pontuacao = c.fetchone()[0] + 1 #seleciona oprimeirovalordo resultado
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H:%M:%S'))    
    c.execute("UPDATE dados SET pontos = (?), data = (?) WHERE nome = (?)",(pontuacao,date,winer))
    #c.execute('UPDATE dados set ( nome, data, pontos) values (?, ?, ?) WHERE NOME = SNAKE2', ("snake2" , date, unix))     
#==============================================================================
# sempre colocar .commit() para atualizar o banco de  dados
#==============================================================================
    connection.commit()

    
#==============================================================================
# main
#==============================================================================
create_tab()
dateentry()
#atualizar("snake1")
c.close()
connection.close()