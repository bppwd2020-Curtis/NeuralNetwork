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
	pygame.draw.rect(screen,red,(0,0,screen.get_width()/2,screen.get_height()/3),0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    clock.tick(30) 
    screen.fill(white)
    draw_red(255)
    pygame.display.flip()

