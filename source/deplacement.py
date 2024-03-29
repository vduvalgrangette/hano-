# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:52:05 2024

@author: merrinicolasdematons
"""

from tkinter import*
from PIL import Image, ImageTk
import time as time

#fonctions de déplacement pour la suite du programme servant dans les différents modes de jeu


def deplacer(lA:[int],lB:[int]):
    '''hyp :l et l2 sont des listes
    Retourne les liste en ayant déplacé le dernier element de l dans l2'''
    lB.append(lA[len(lA)-1])
    del lA[len(lA)-1]
    return lA, lB

def mouvementv(plan,perso,y):
    '''deplace une image perso d'un canevas plan, à la verticale de y'''
    if y>0:
        for i in range(y//5):
            plan.move(perso.canevas,0,5)
            plan.update()
            time.sleep(0.004)
    else :
        for i in range(-y//5):
            plan.move(perso.canevas,0,-5)
            plan.update()
            time.sleep(0.004)
    plan.move(perso.canevas,0,y%5)

def mouvementh(plan,perso,x):
    '''deplace une image perso d'un canevas plan, à l horizontale de x'''
    if x>0:
        for i in range(x//5):
            plan.move(perso.canevas,5,0)
            plan.update()
            time.sleep(0.004)
    else :
        for i in range(-x//5):
            plan.move(perso.canevas,-5,0)
            plan.update()
            time.sleep(0.004)
    plan.move(perso.canevas,0,x%5)


def  animation2h(plan,perso1,perso2,x,costume):
    '''deplace le sportif avec ses différents costumes et le disque qu'il porte de x pixels à l'horizontal'''
    if x>0:
        perso1.nouveaudebut(perso1.x, perso1.y, costume[4])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(costume[0])
        plan.update()
        for i in range(x//5):
            plan.move(perso1.canevas,5,0)
            plan.move(perso2.canevas,5,0)
            plan.update()
            time.sleep(0.001)
    else :
        perso1.nouveaudebut(perso1.x, perso1.y, costume[5])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(costume[0])
        plan.update()
        for i in range(-x//5):
            plan.move(perso1.canevas,-5,0)
            plan.move(perso2.canevas,-5,0)
            plan.update()
            time.sleep(0.001)
    plan.move(perso1.canevas,0,x%5)
    plan.move(perso2.canevas,0,x%5)
    perso1.x+=x
    perso2.x+=x
    perso1.nouveaudebut(perso1.x, perso1.y, costume[6])
    plan.tag_lower(perso1.canevas)
    plan.tag_lower(costume[0])
    plan.update()

def animationh(plan,perso,x,costume):
    '''deplace le sportif avec ses différents costumes de x pixels à l'horizontal'''
    if x>0:
        perso.nouveaudebut(perso.x, perso.y, costume[2])
        plan.tag_lower(perso.canevas)
        plan.tag_lower(costume[0])
        plan.update()
        for i in range(x//5):
            plan.move(perso.canevas,5,0)
            plan.update()
            time.sleep(0.001)
    else :
        perso.nouveaudebut(perso.x, perso.y, costume[3])
        plan.tag_lower(perso.canevas)
        plan.tag_lower(costume[0])
        plan.update()
        for i in range(-x//5):
            plan.move(perso.canevas,-5,0)
            plan.update()
            time.sleep(0.001)
    plan.move(perso.canevas,0,x%5)
    perso.x+=x
    perso.nouveaudebut(perso.x, perso.y, costume[1])
    plan.tag_lower(perso.canevas)
    plan.tag_lower(costume[0])
    plan.update()

def soulever(plan,perso1,perso2,y,lever):
    '''le sportif soulève le disque'''
    if y<0:
        temps=0
        perso1.y+=40
        perso1.nouveaudebut(perso1.x, perso1.y,lever[1])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(lever[0])
        a=1
        plan.update()
        for i in range(-y//5):
            plan.move(perso2.canevas,0,-5)
            temps+=1
            if temps==7 and a<5:
                if a==3:
                    perso1.y-=40
                perso1.nouveaudebut(perso1.x, perso1.y, lever[a])
                plan.tag_lower(perso1.canevas)
                plan.tag_lower(lever[0])
                temps=0
                a+=1
            plan.update()
            time.sleep(0.004)
        perso1.nouveaudebut(perso1.x, 300, lever[4])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(lever[0])
        plan.update()
    else :
        temps=0
        perso1.y+=40
        perso1.nouveaudebut(perso1.x, perso1.y,lever[1])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(lever[0])
        a=1
        plan.update()
        for i in range(y//5):
            plan.move(perso2.canevas,0,5)
            temps+=1
            if temps==7 and a<5:
                if a==3:
                    perso1.y-=40
                perso1.nouveaudebut(perso1.x, perso1.y, lever[a])
                plan.tag_lower(perso1.canevas)
                plan.tag_lower(lever[0])
                temps=0
                a+=1
            plan.update()
            time.sleep(0.004)
        perso1.nouveaudebut(perso1.x, 300, lever[4])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(lever[0])
        plan.update()
    
    
def deposer(plan,perso1,perso2,y,poser):
    '''le sportif dépose le disque'''
    if y>0:
        temps=0
        perso1.y+=40
        perso1.nouveaudebut(perso1.x, perso1.y-10,poser[1])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(poser[0])
        a=1
        plan.update()
        for i in range(y//5):
            plan.move(perso2.canevas,0,5)
            temps+=1
            if temps==7 and a<3:
                a+=1
                perso1.y+=40
                perso1.nouveaudebut(perso1.x, perso1.y+10, poser[a])
                plan.tag_lower(perso1.canevas)
                plan.tag_lower(poser[0])
            plan.update()
            time.sleep(0.004)
        perso1.y-=80
        for j in range(3):
            a+=1
            perso1.nouveaudebut(perso1.x, perso1.y, poser[a])
            plan.tag_lower(perso1.canevas)
            plan.tag_lower(poser[0])
            plan.update()
            time.sleep(0.08)
        perso1.nouveaudebut(perso1.x, 300, poser[5])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(poser[0])
        plan.update()
    else :
        temps=0
        perso1.y+=40
        perso1.nouveaudebut(perso1.x, perso1.y-10,poser[1])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(poser[0])
        a=1
        plan.update()
        for i in range(-y//5):
            plan.move(perso2.canevas,0,-5)
            temps+=1
            if temps==7 and a<3:
                a+=1
                perso1.y+=40
                perso1.nouveaudebut(perso1.x, perso1.y+10, poser[a])
                plan.tag_lower(perso1.canevas)
                plan.tag_lower(poser[0])
            plan.update()
            time.sleep(0.004)
        perso1.y-=80
        for j in range(3):
            a+=1
            perso1.nouveaudebut(perso1.x, perso1.y, poser[a])
            plan.tag_lower(perso1.canevas)
            plan.tag_lower(poser[0])
            plan.update()
            time.sleep(0.08)
        perso1.nouveaudebut(perso1.x, 300, poser[5])
        plan.tag_lower(perso1.canevas)
        plan.tag_lower(poser[0])
        plan.update()