import pygame, sys, random
from pygame import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 600
check = 0

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

class buff():
    def __init__(self):
         self.distance = 250
         self.ls = []
         for i in range (5):
             lane = random.randint(check,3)
             self.ls.append([lane,y])


