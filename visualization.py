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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    clock.tick(30) 
    screen.fill(white)
    draw_red(255)
    draw_green(255)
    draw_blue(255)
    




    pygame.display.flip()

