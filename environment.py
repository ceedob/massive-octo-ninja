import entity, pygame
class platform (entity.entity):
	def __init__(self):
		self.height = 20
		
	type = "PLATFORM"
	def draw(self, window,scroll):
		pygame.draw.rect(window,(0,255,0),(self.x-scroll, self.y, self.width, self.height))
		
	def blocking(self, player):
	   if player.up>=0:
		if self.x < player.x and self.x + self.width > player.x:
		 if self.y - (player.y+player.height/2) < 5 and self.y - player.y > 0:
		  return self.impassable
		 else:
		  return False
		else:
		 return False
		
class wall(entity.entity):
	def __init__(self):
		self.width=20
		
	type = "WALL"
	def draw(self, window,scroll):
		pygame.draw.rect(window,(0,255,0),(self.x-scroll, self.y, self.width, self.height))

	def blocking(self, player):
	   if player.side > 0 : #going right
		if (self.x - (player.x + player.width/2) > -2 and self.x - (player.x + player.width/2) < 5):
		 if (self.y - player.y) <= 0 and (self.y+self.height - (player.y+player.height/2)) >= 0:
		  return self.impassable
		 else:
		  return False
		else:
		 return False
	   elif player.side < 0:
	    if (self.x+self.width - (player.x - player.width/2) > -2 and self.x+self.width - (player.x - player.width/2) < 5):
		 if (self.y - player.y) <= 0 and (self.y+self.height - (player.y+player.height/2)) >= 0:
		  return self.impassable
		 else:
		  return False
	    else:
		 return False
	   else:
	    return False
