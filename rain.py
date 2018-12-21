import pygame
import time
import random

class Drop:
	# Constructor
	def __init__(self):
		self.p1 = int(random.random()*win_width) + 1
		self.p2 = int(random.random()*(max_drop-min_drop)) + min_drop
		self.length = 20
		self.width = 2
		self.speed = int(random.random()*(40-10)) + 10

	def draw(self):
		pygame.draw.rect(win, purple, pygame.Rect(self.p1, self.p2, self.width, self.length))

	def undraw(self):
		pygame.draw.rect(win, background, pygame.Rect(self.p1, self.p2, self.width, self.length))

	def move(self):
		self.p2 = self.p2 + self.speed






# Set parameters
max_drop = -500
min_drop = -100

win_width = 800
win_height = 480

background = (230, 230, 250)
purple = (183, 43, 226)

drops = 400

# Initiate pygame
pygame.init()
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Purple Rain')
win.fill(background)

drps = []
for i in range(drops):
	drps.append(Drop())

for dr in drps:
	dr.draw()
pygame.display.update()

# Game loop
run = True
while run:
	pygame.time.delay(100)

	for dr in drps:	
		dr.undraw()
		dr.move()
		dr.draw()

		if (dr.p2 > win_height):
			dr.p2 = int(random.random()*(max_drop-min_drop)) + min_drop
			dr.p1 = int(random.random()*win_width) + 1
			dr.speed = int(random.random()*(40-10)) + 10

	pygame.display.update()

	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			run = False