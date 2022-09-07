#Autumn Leaves Rain.

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

pygame.display.set_caption("The Falling Leaves...")

#screen settings.
screen_width = 900
screen_height = 400
screen_backcolor = (92, 61, 46)
screen = pygame.display.set_mode((screen_width, screen_height),0,32)
screen.fill(screen_backcolor)

#list of tracks.
playlist = []							
							 
for value in range(1,9):
	playlist.append(str(value) + ".ogg")

#lengths of tracks
lengths = [278000, 658000, 213000, 422000, 
340000, 379000, 445000, 464000, 305000] 

#picks a random track from playlist each time.	
for p in playlist:
	r = random.choice(playlist)
	pygame.mixer.music.load(r)				

#loads background music.
pygame.mixer.music.play(-1, 0.0)		

#dictionary that contains each track within playlist paired to its length.
lengths_playlist = dict(zip(playlist, lengths))

#variable for event to quit program after track ends.
LENGTH = lengths_playlist.get(r)

#list of leaf pics to be used in Leaf class.
leaves = []								
for value in range(0,9):
	leaves.append(str(value) + ".png")

#class that defines and controls Leaf sprites.	
class Leaf(pygame.sprite.Sprite):		
	
	def __init__(self):
		
		pygame.sprite.Sprite.__init__(self)
		
		"""object's apeparance"""
		self.path = random.choice(leaves)
		self.image = pygame.image.load(self.path)
		self.rect = self.image.get_rect()
		"""object's position"""
		self.rect.x = random.randint(0, screen_width-100)
		self.rect.y = -150

clock = pygame.time.Clock()

#list to control draw and update within loop.
rains = []							

#each sprite group contains leaves falling at different speeds.
rain1 = pygame.sprite.Group()			 
rains.append(rain1)	
										
rain2 = pygame.sprite.Group()					
rains.append(rain2)						
												
rain3 = pygame.sprite.Group()
rains.append(rain3)								

#events t/control when e/type o/leaf appears (refactoring needed).
LEAF1 = pygame.USEREVENT + 0			
pygame.time.set_timer(LEAF1, 500)

LEAF2 = pygame.USEREVENT + 1
pygame.time.set_timer(LEAF2, 2000)

LEAF3 = pygame.USEREVENT + 2
pygame.time.set_timer(LEAF3, 10000)

TRACKLENGTH = pygame.USEREVENT + 3
pygame.time.set_timer(TRACKLENGTH, LENGTH)

#distance at which Leaf sprite is removed from group.
kill_distance = screen_height + 50		

#falling leaves loop. (refactoring needed).
while True:	

	screen.fill(screen_backcolor)

	for event in pygame.event.get():
		
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
		if event.type == TRACKLENGTH:
			pygame.quit()
			sys.exit()

		if event.type == LEAF1:
	
			leaf1 = Leaf()
			rain1.add(leaf1)
		
		if event.type == LEAF2:
	
			leaf2 = Leaf()
			rain2.add(leaf2)
			
		if event.type == LEAF3:
	
			leaf3 = Leaf()
			rain3.add(leaf3)
			
	for a in rain1:
				
		a.rect.y += 1
	
		if a.rect.y == kill_distance:	
			a.kill()
			
	for b in rain2:
				
		b.rect.y += 2
	
		if b.rect.y == kill_distance:	
			b.kill()
	
	for c in rain3:
				
		c.rect.y += 5
	
		if c.rect.y == kill_distance:	
			c.kill()
	
	for rain in rains:
		
		rain.update()
		rain.draw(screen)
	
	pygame.display.flip()
	pygame.display.update()

	clock.tick(40)


### Things to consider:
# Event timer and gravities: somehow, not all gravities work for sprites to be killed within loop when specified, but unable to understand why. The following are pairs of vertical motion and time frames that work: (5:2500,5000), (1:500,1000), (2:2000,4000).
# A list of other nice RGB colors that can be used in the background: rgb(165,113,100) rgb(176, 155, 113) rgb(173, 139, 115) rgb(112, 79, 79) rgb(92, 61, 46)
