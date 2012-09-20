import math, pygame

def HSVtoRGB(H):
	r,g,b=0,0,0
	i = H/85 
	f = (H/(85.0)) - i			#// factorial part of h
	p = 255
	v = 255
	inc = 255 * f
	dec = 255 * (1-f)
		#print (H/51),i,f
	if i == 0: #RB to RG 
			r = 255
			g = inc
			b = dec
	elif i == 1: #RG to GB
			r = dec
			g = 255
			b = inc
	elif i == 2: #GB to RB
			r = inc
			g = dec
			b = 255
	else:
			r = 255
			g = 0
			b = 255

	return (int(r),int(g),int(b))
		


class entity (object):
	x = 0
	y = 0
	speed = 0
	impassable = True
	height = 0
	width = 0
	type = None
	damage = 100
	def __init__(self):
		pass
		
	def blocking(self, player):
		if math.sqrt(((self.x+self.width/2)-(player.x))**2+((self.y+self.height/2)-(player.y))**2)<player.width:
			return True
		else:
			return False

class bonus(entity):
	def __init__(self):
		self.width=10
		self.height=10
		
	type = "BONUS"
	ticks = 170
	def draw(self, window,scroll):
		pygame.draw.rect(window,HSVtoRGB(int(self.ticks)%255),(self.x-scroll, self.y, self.width, self.height))
		self.ticks += 0.2
	
	def clear(self):
		del(self)