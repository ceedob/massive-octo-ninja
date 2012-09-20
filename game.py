import pygame, sys,os, math
import Player, environment, entity
from pygame.locals import * 
from pygame.draw import *

pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
fpsClock = pygame.time.Clock()
scroll = 0
scrolling = 0

player = Player.player()
player.x=150
player.window = window.get_height()

entities = [environment.platform(),environment.platform(),environment.platform(),environment.wall(),entity.bonus(), environment.platform(), environment.wall(),environment.platform(),environment.platform(),environment.platform(),environment.platform(),environment.wall()]
entities[0].x = 100
entities[0].y = 300
entities[0].width = 200
entities[1].x = 300
entities[1].y = 500
entities[1].width = 400
entities[2].x = 100
entities[2].y = 700
entities[2].width = 101
entities[3].x = 250
entities[3].y = 100
entities[3].height = 200
entities[4].x = 1950
entities[4].y = 200
entities[5].x = 900
entities[5].y = 600
entities[5].width = 150
entities[6].x = 750
entities[6].y = 250
entities[6].height = 450
entities[7].x=1000
entities[7].y=400
entities[7].width=500
entities[8].x=1500
entities[8].y=700
entities[8].width = 400
entities[9].x=1800
entities[9].y=300
entities[9].width=600
entities[10].x = 1950
entities[10].y = 650
entities[10].width = 800
entities[11].x = 2600
entities[11].y = 250
entities[11].height = 300

def input(events): 
   global player

   for event in events: 
      if event.type == QUIT: 
         sys.exit(0)
         
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
         sys.exit(0)
         
        if event.key == K_a or event.key == K_LEFT:
         player.left = True
        elif event.key == K_d or event.key == K_RIGHT:
         player.right = True
        elif event.key == K_w or event.key == K_UP:
          player.jump()
           
      elif event.type == KEYUP:
         if event.key == K_a or event.key == K_LEFT:
          player.left=False
         elif event.key == K_d or event.key == K_RIGHT:
          player.right=False
          
      else:
      	pass 
         #print event 

while True: 
	
	window.fill((0,0,255))
	
	player.tick(entities)
	
	
	for e in entities:
		e.draw(window,scroll)
	
	if player.x-scroll > window.get_width()/2:
		if player.x-scroll > window.get_width() or player.x-scroll < 0: 
			scrolling +=5
		elif scrolling <= 10:
			scrolling += 0.5
	elif player.x-scroll < window.get_width()/10:
		if player.x-scroll > window.get_width() or player.x-scroll < 0: 
			scrolling +=-5
		elif scrolling >= -10:
			scrolling += -0.5
	elif scrolling>0:
		scrolling +=-0.1
	elif scrolling<0: 
		scrolling+=0.1
	
	scroll += scrolling
	if scroll < 0: scroll = 0
	player.draw(window,scroll)
			
	input(pygame.event.get())  
	pygame.display.update()
	fpsClock.tick(30)
	
