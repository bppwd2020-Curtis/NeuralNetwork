import os,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np
from Neuron import *
from NeuralNetMath import *
from NeuralNetLayer import *
from NeuralNetwork import *

#Neural Net Part
n1 = Neuron("Red")
n2 = Neuron("Green")
n3 = Neuron("Blue")


neurons = [n1,n2,n3]
inputLayer = NeuralNetLayer(neurons)

nn = NeuralNetwork([inputLayer],9999,0.001)

mystery = [2.55,2.55,2.55]

data = [
		#Colors That Look Good in Black
		[2.55,2.55,0,1],#yellow
		[0,2.55,0,1],#lime
		[2.55,2.55,2.55,1],#white
		[0,2.55,2.55,1],#cyan
		#Colors That Look good on White
		[1.28,0,0,0],#maroon
		[0,0,0,0],#black
		[1.28,1.28,1.28,0],#gray
		[0,0,1.28,0]#Navy
		]

nn.train_all(data, reLu)

mystery = [2.55,2.55,2.55]

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
pygame.display.set_caption("RGB Neural Network")

def draw_text(string,size,color,coord):
	font = pygame.font.SysFont("arial",size)
	text = font.render(string,True,color)
	screen.blit(text,(coord[0] - text.get_width() // 2, coord[1] - text.get_height() // 2))

def draw_red(r):
	#draws based on red value
	pygame.draw.rect(screen,(r*100,0,0),(0,0,screen.get_width()/2,screen.get_height()/3),0)

def draw_green(g):
	#draws based on green value
	green_y = (screen.get_height()/3)
	pygame.draw.rect(screen,(0,g*100,0),(0,green_y,screen.get_width()/2,screen.get_height()/3),0)

def draw_blue(b):
	#draws based on blue value
	blue_y = 2 * (screen.get_height()/3)
	pygame.draw.rect(screen,(0,0,b*100),(0,blue_y,screen.get_width()/2,screen.get_height()/3),0)

def draw_rgb(r,g,b):
	#Use when individual Values
	draw_red(r)
	draw_green(g) 
	draw_blue(b) 

def draw_output(r,g,b,back):
	rect = pygame.Rect(screen.get_width()/2,0,screen.get_width()/2,screen.get_height())
	pygame.draw.rect(screen,back,rect,0)
	draw_text("Test",50,(r*100,g*100,b*100),rect.center)

def draw_total(r,g,b,back):
	draw_rgb(r,g,b)
	draw_output(r,g,b,back)



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	clock.tick(30) 
	screen.fill(white)

	if(reLu(nn.neuralNetLayers[0].getPrediction(mystery)) <= 0):
		back = white
	elif(reLu(nn.neuralNetLayers[0].getPrediction(mystery)) > 0):
		back = black

	draw_total(mystery[0],mystery[1],mystery[2],back)

	pressed = pygame.key.get_pressed()

	if(pressed[pygame.K_i]):
		print("Input New RGB Values: ")
		mystery[0] = float(input("Red: "))/100
		mystery[1] = float(input("Green: "))/100
		mystery[2] = float(input("Blue: "))/100

	pygame.display.flip()

 