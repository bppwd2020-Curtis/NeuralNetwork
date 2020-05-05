import os,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
white = 255, 255, 255

screen = pygame.display.set_mode(pygame.display.list_modes(depth=0, flags=pygame.FULLSCREEN)[1])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    pygame.display.flip()