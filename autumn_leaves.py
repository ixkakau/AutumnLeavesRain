#Autumn Leaves Rain.

import sys, pygame, time, random

from pygame.locals import *

pygame.init()

width = 1000

class Settings():
	""" storage of settings """
 
	def __init__(self):
		"""starts settings"""
		
		self.screen_width = width 						      #window width
		self.screen_height = 500						      #window height
		self.maincolor = (165,113,100)					              #background color
leaves = []										      #list with different leaf images

for value in range(0,9):								      #loop that generates leaves images list
	leaves.append(str(value) + ".png")
		
class Leaves():
	
	def __init__(self, pantalla):
		"""attributes for each leaf from leaves_rain"""
		
		super(Leaves, self).__init__()				
		
		self.pantalla = pantalla						      #makes leaf appear on screen
		self.path = random.choice(leaves)				              #path to leaf pic
		self.image = pygame.image.load(self.path)		          	      #makes leaf image from path
			
		self.rect = self.image.get_rect()				              #gets leaf image rectangle attributes
		self.pantalla_rect = pantalla.get_rect()		                      #gets screen dimentions
		
		self.rect.right = random.randint(120, width)	        #leaf image right horizontal position
		self.rect.top = self.pantalla_rect.top - 180	        #leaf image top vertical position
		
	def update(self):
		"""update leaves' position based on movement by gravity"""
			
	def blitme(self):
		"""draws the leaves at location specified by self.rect"""
		self.pantalla.blit(self.image, self.rect)

def autumn_leaves_rain():
	"""autumn_leaves main funcion"""
	
	ti_settings = Settings()
	
	pantalla = pygame.display.set_mode(					        #window settings
	(ti_settings.screen_width, 
	ti_settings.screen_height))
	
	caption = pygame.display.set_caption(				          	#window main bar message
	"The falling leaves...")
	
	playlist = ['0.wav', '1.wav', '2.wav', 
              '3.wav', '4.wav', '5.wav']                				#list of tracks
	
	for track in playlist:
	
		pygame.mixer.music.load(random.choice(playlist))		       	#random pick from list of tracks
	
	pygame.mixer.music.play(-1, 0.0)					
	
	clock = pygame.time.Clock()							#sets clock for animation to happen
		
	gravities = []									#list with different gravity values for leaves to fall at different speeds
	
	leaf_objects = []								#list with different leaf objects
	
	def autumn_leaf():
		"""creates each leaf object"""
						
		pantalla.fill(ti_settings.maincolor)			  		#updates the screen after leaf object passes through
		
		for (obj, gravity) in zip(leaf_objects, 				#loop generates a falling leaf image with random gravity and image
									gravities):
		
			obj.rect.bottom += gravity          				#leaves fall
			obj.update()                        
			obj.blitme()                       
			
		pygame.display.flip()
		pygame.display.update()
									
	while True:									 #loop that controls leaves rain
						
		gravities.append(random.randint(1,3))
		gravities.append(1)			              			 #random gravity to change falling speed each time new leaves are generated
		
		for leaf in range(40):							 #creates several leaves from function autumn_leaf()
			
			leaf = Leaves(pantalla)
			leaf_objects.append(leaf)
			autumn_leaf()
			
			clock.tick(70)							 #frames per second
				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

autumn_leaves_rain()
