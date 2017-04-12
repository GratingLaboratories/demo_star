#!/usr/bin/python3
# encoding=utf-8

"""
                         _____  _____  _____  _____  _____         _____
           /////  /     /____/ /___ / /___ / /_ __/ /_ __/ /|  // /____/
           ////  //    //___  //__// //__//   //     //   / | // //___
          ////  //    // \ / / ___/ /___ /   //     //   //||// // \ /
          ///  ///   //__// //\\   //  //   //   __//_  // | / //__//
         ///  ///   /____/ //  \\ //  //   //   /____/ //  |/ /____/
         //  ////      _   _   _   _   _  _ _  _   _  _ _  __  __
        //  ////  |   |_| |_) / \ |_) |_|  |  / \ |_)  |  |_  (_
        /  /////  |__ | | |_) \_/ | \ | |  |  \_/ | \ _|_ |__ __)
    =================================================================
      Use <ESC> to quit.
"""

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((1920, 1080), FULLSCREEN)
SURFACE = pygame.display.get_surface()
FPS = 60
running = True

star1 = pygame.image.load('star1.png').convert(24)
star1.set_colorkey(star1.get_at((0, 0)))
star2 = pygame.image.load('star2.png').convert(24)
star2.set_colorkey(star2.get_at((0, 0)))
bigstar = pygame.image.load('bigstar.png').convert(24)
bigstar.set_colorkey(bigstar.get_at((0, 0)))

screens = [pygame.image.load('black.png')] + [pygame.Surface((1920, 1080)) for i in range(12)]

# order = [0, 1, 1, 1, 0, 2, 2, 2, 0, 3, 3, 3, 0]
order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0]

layer1 = 4
layer2 = 10
layer3 = 14

for j in range(12):
    i = j + 1
    #high
    subsurf = star1.subsurface(pygame.Rect(12*layer1-i*layer1, 0, 1920-12*layer1+i*layer1, 1080))
    screens[i].blit(subsurf, pygame.Rect(0, 0, 1920-12*layer1+i*layer1, 1080))
    subsurf = star2.subsurface(pygame.Rect(12*layer2-i*layer2, 0, 1920-12*layer2+i*layer2, 1080))
    screens[i].blit(subsurf, pygame.Rect(0, 0, 1920-12*layer2+i*layer2, 1080))
    subsurf = bigstar.subsurface(pygame.Rect(12*layer3-i*layer3, 0, 1920-12*layer3+i*layer3, 1080))
    screens[i].blit(subsurf, pygame.Rect(0, 0, 1920-12*layer3+i*layer3, 1080))

list135211 = []
x = 0.0
while x < 1910:
    list135211.append(int(x))
    x += 13.5211

for x in list135211:
    for y in range(1080):
        for i in range(13):
            color = screens[order[i]].get_at((x+i, y))
            SURFACE.set_at((x+i, y), color)
pygame.display.flip()

'''
for x in list135211[:10] + list135211[-10:]:
    for i in range(13):
        if order[i] == 1 and x in list135211[0:3] + list135211[-10:-7]:
            pygame.draw.line(SURFACE, 0x00ff00, (x+i, i*1080//13), (x+i, (i+1)*1080//13))
        elif order[i] == 2 and x in list135211[3:6] + list135211[-7:-4]:
            pygame.draw.line(SURFACE, 0x00ff00, (x+i, i*1080//13), (x+i, (i+1)*1080//13))
        elif order[i] == 3 and x in list135211[6:9] + list135211[-4:-1]:
            pygame.draw.line(SURFACE, 0x00ff00, (x+i, i*1080//13), (x+i, (i+1)*1080//13))
pygame.display.flip()
'''

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
    clock.tick(FPS)
