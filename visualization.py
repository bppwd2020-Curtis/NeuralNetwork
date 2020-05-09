import os,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame




pygame.init()

size = width, height = 320, 240
speed = [2, 2]
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(pygame.display.list_modes(depth=0, flags=pygame.FULLSCREEN)[2])

def draw_red(r):
	#draws based on red value
	pygame.draw.rect(screen,(r,0,0),(0,0,screen.get_width()/2,screen.get_height()/3),0)

def draw_green(g):
	#draws based on green value
	green_y = (screen.get_height()/3)
	pygame.draw.rect(screen,(0,g,0),(0,green_y,screen.get_width()/2,screen.get_height()/3),0)

def draw_blue(b):
	#draws based on blue value
	blue_y = 2 * (screen.get_height()/3)
	pygame.draw.rect(screen,(0,0,b),(0,blue_y,screen.get_width()/2,screen.get_height()/3),0)

def draw_rgb(r,g,b):
	#Use when individual Values
	draw_red(r)
	draw_green(g) 
	draw_blue(b) 

def draw_RGB(rgb):
	#Use when passed as an array
	draw_red(rgb[0])
	draw_green(rgb[1])
	draw_blue(rgb[2])

def draw_output(r,g,b):
	pygame.draw.rect(screen,(r,g,b),(screen.get_width()/2,0,screen.get_width()/2,screen.get_height()),0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    clock.tick(30) 
    screen.fill(white)
    draw_output(128,0,128)
    




    pygame.display.flip()

