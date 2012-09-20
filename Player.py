import entity, pygame
from pygame.locals import * 
from entity import *

class player(entity):
	img = pygame.image.load("char.png")
	def __init__(self):
		self.img = pygame.image.load("char.png")
		
	height = 100
	width = 90
	y= 300
	
	accel = 1
	
	window = 0
	
	left, right = False, False
	side, up = 0, 0 #up is down
	
	jumping = 0
	
	on=False
	
	color = 170;
	
	friction=0.85
	
	def tick(self, entities):
		
		if self.jumping > 0:
			self.jumping +=-1
			self.up+=-self.accel*3
		else:
			self.up += self.accel
			
		if self.left == True:
			self.side += -self.accel*1.6
		if self.right == True:
			self.side += self.accel*1.6
			
		if self.y > self.window and self.up > 0:
			self.up = 0
		
		allowedDown = True
		for e in entities:
			if e.blocking(self) and e.type == "PLATFORM":
				allowedDown = False
				self.damage +=-self.up
				self.up = 0
				self.y = e.y - self.height/2
				#self.on = True
			elif e.blocking(self) and e.type == "WALL":
				if self.side > 0:
					self.x = e.x-self.width/2
				else:
					self.x = e.x+e.width+self.width/2
				self.side = 0
				if self.up<0:self.up*=1.09
				#self.on = True
			elif e.blocking(self) and e.type == "BONUS":
				entities.remove(e)
				self.on = True
		self.x += self.side
		self.y += self.up
		
		if self.on:
			self.color+=5
			self.color%=255
		
		self.side *=self.friction
		
	def jump(self):
		if self.jumping == 0 and self.up==0:
			self.jumping = 6
		
		
	def draw(self, window, scroll):
		if self.y-self.width/2 > 0:
			if self.on:
				pygame.draw.rect(window,HSVtoRGB(self.color),(self.x-self.width/2-scroll, self.y-self.height/2, self.width, self.height))
			else:
				window.blit(self.img, (self.x-self.width/2-scroll, self.y-self.height/2, self.width, self.height))
				
				#pygame.draw.rect(window,(0,0,0),(self.x-self.width/2-scroll, self.y-self.height/2, self.width, self.height))
		else:
			if self.on:
				pygame.draw.polygon(window,HSVtoRGB(self.color),[(self.x-scroll,0),(self.x+self.width/(1+math.sqrt(abs(self.y))/10)-scroll,self.height),(self.x-scroll,self.height/2),(self.x-self.width/(1+math.sqrt(abs(self.y))/10)-scroll,self.height)])
			else:
				pygame.draw.polygon(window,(0,0,0),[(self.x-scroll,0),(self.x+self.width/(1+math.sqrt(abs(self.y))/10)-scroll,self.height),(self.x-scroll,self.height/2),(self.x-self.width/(1+math.sqrt(abs(self.y))/10)-scroll,self.height)])
			