#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit


background_image = '../image/sushiplate.jpg'
sprite_image = '../image/fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image)

# clock对象
clock = pygame.time.Clock()

x = 0
speed = 250

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    if x > 640:
        x -= 640

    pygame.display.update()