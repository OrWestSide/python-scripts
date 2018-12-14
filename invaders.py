import random
import pygame
import time

# Define classes
class Shield:
	
	# Shield constructor
	def __init__(self, p1,p2):
		self.health = 12
		self.p1 = p1
		self.p2 = p2
		self.size = 60
	
	# Function that decreases health when hit
	def getHit(self):
		self.health = self.health - 1
	
	# Draw shield depending on health
	def draw(self):
		if (self.health <= 0):
			pygame.draw.polygon(win, (0,0,0),  [(self.p1,self.p2), (self.p1+20,self.p2-20), (self.p1+40,self.p2-20), (self.p1+60,self.p2)])
			pygame.display.update()
		elif (self.health <= 3):
			pygame.draw.polygon(win, (0,0,0), [(self.p1+5,self.p2-5), (self.p1+20,self.p2-20), (self.p1+40,self.p2-20), (self.p1+55,self.p2-5)])
			pygame.display.update()
		elif (self.health <= 6):
			pygame.draw.polygon(win, (0,0,0), [(self.p1+10,self.p2-10), (self.p1+20,self.p2-20), (self.p1+40,self.p2-20), (self.p1+50,self.p2-10)])			
			pygame.display.update()
		elif (self.health <= 9):
			pygame.draw.polygon(win, (0,0,0), [(self.p1+15,self.p2-15), (self.p1+20,self.p2-20), (self.p1+40,self.p2-20), (self.p1+45,self.p2-15)])			
			pygame.display.update()
		else:
			pygame.draw.polygon(win, (0,200,0), [(self.p1,self.p2), (self.p1+20,self.p2-20), (self.p1+40,self.p2-20), (self.p1+60,self.p2)])
			pygame.display.update()

class Minion1:
	# Minion1 constructior
	def __init__(self, p1, p2):
		self.health = 1
		self.speed = 2
		self.p1 = p1
		self.p2 = p2
		self.size = 12

	# Sets health to zero when hit
	def getDestroyed(self):
		self.health = 0

	# Draw minion
	def draw(self):
		if (self.health == 1):
			# Body
			pygame.draw.polygon(win, (255,255,255), [(self.p1,self.p2), (self.p1+6,self.p2-6), (self.p1+12,self.p2), (self.p1+6,self.p2+6)])
			# Left leg
			pygame.draw.line(win, (255,255,255), (self.p1+3,self.p2+3), (self.p1,self.p2+6))
			pygame.draw.line(win, (255,255,255), (self.p1,self.p2+6), (self.p1+3,self.p2+9))
			# Right leg
			pygame.draw.line(win, (255,255,255), (self.p1+9,self.p2+3), (self.p1+12,self.p2+6))
			pygame.draw.line(win, (255,255,255), (self.p1+12,self.p2+6), (self.p1+9,self.p2+9))
			# Eyes
			pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+3,self.p2))
			pygame.draw.line(win, (0,0,0), (self.p1+9,self.p2), (self.p1+9,self.p2))
		else:
			# Body
			pygame.draw.polygon(win, (0,0,0), [(self.p1,self.p2), (self.p1+6,self.p2-6), (self.p1+12,self.p2), (self.p1+6,self.p2+6)])
			# Left leg
			pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2+3), (self.p1,self.p2+6))
			pygame.draw.line(win, (0,0,0), (self.p1,self.p2+6), (self.p1+3,self.p2+9))
			# Right leg
			pygame.draw.line(win, (0,0,0), (self.p1+9,self.p2+3), (self.p1+12,self.p2+6))
			pygame.draw.line(win, (0,0,0), (self.p1+12,self.p2+6), (self.p1+9,self.p2+9))
			# Eyes
			pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+3,self.p2))
			pygame.draw.line(win, (0,0,0), (self.p1+9,self.p2), (self.p1+9,self.p2))

	# Erase or UNDRAW minion
	def unDraw(self):
		# Body
		pygame.draw.polygon(win, (0,0,0), [(self.p1,self.p2), (self.p1+6,self.p2-6), (self.p1+12,self.p2), (self.p1+6,self.p2+6)])
		# Left leg
		pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2+3), (self.p1,self.p2+6))
		pygame.draw.line(win, (0,0,0), (self.p1,self.p2+6), (self.p1+3,self.p2+9))
		# Right leg
		pygame.draw.line(win, (0,0,0), (self.p1+9,self.p2+3), (self.p1+12,self.p2+6))
		pygame.draw.line(win, (0,0,0), (self.p1+12,self.p2+6), (self.p1+9,self.p2+9))
		# Eyes
		pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+3,self.p2))
		pygame.draw.line(win, (0,0,0), (self.p1+9,self.p2), (self.p1+9,self.p2))

	def move(self):
		self.p1 = self.p1 + self.speed

class Minion2:
	# Minion2 constructor
	def __init__(self, p1, p2):
		self.health = 1
		self.speed = 2
		self.p1 = p1
		self.p2 = p2
		self.size = 20

	def getDestroyed(self):
		self.health = 0

	def draw(self):
		if (self.health == 1):
			# Body
			pygame.draw.polygon(win, (255,255,255), [(self.p1, self.p2), (self.p1,self.p2-5), (self.p1+5,self.p2-10), (self.p1+15,self.p2-10), (self.p1+20,self.p2-5),
				 (self.p1+20,self.p2), (self.p1+15,self.p2-4), (self.p1+5,self.p2-4)])
			# Left leg
			pygame.draw.line(win, (255,255,255), (self.p1+6,self.p2-4), (self.p1+3,self.p2))
			pygame.draw.line(win, (255,255,255), (self.p1+3,self.p2), (self.p1+6,self.p2+4))
			# Right leg
			pygame.draw.line(win, (255,255,255), (self.p1+14,self.p2-4), (self.p1+17,self.p2))
			pygame.draw.line(win, (255,255,255), (self.p1+17,self.p2), (self.p1+14,self.p2+4))
			# Eyes
			pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-8), (self.p1+6,self.p2-8))
			pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-8), (self.p1+14,self.p2-8))
		else:
			# Body
			pygame.draw.polygon(win, (0,0,0), [(self.p1, self.p2), (self.p1,self.p2-5), (self.p1+5,self.p2-10), (self.p1+15,self.p2-10), (self.p1+20,self.p2-5),
				 (self.p1+20,self.p2), (self.p1+15,self.p2-4), (self.p1+5,self.p2-4)])
			# Left leg
			pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-4), (self.p1+3,self.p2))
			pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+6,self.p2+4))
			# Right leg
			pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-4), (self.p1+17,self.p2))
			pygame.draw.line(win, (0,0,0), (self.p1+17,self.p2), (self.p1+14,self.p2+4))
			# Eyes
			pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-8), (self.p1+6,self.p2-8))
			pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-8), (self.p1+14,self.p2-8))
	
	def unDraw(self):
		# Body
		pygame.draw.polygon(win, (0,0,0), [(self.p1, self.p2), (self.p1,self.p2-5), (self.p1+5,self.p2-10), (self.p1+15,self.p2-10), (self.p1+20,self.p2-5),
			 (self.p1+20,self.p2), (self.p1+15,self.p2-4), (self.p1+5,self.p2-4)])
		# Left leg
		pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-4), (self.p1+3,self.p2))
		pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+6,self.p2+4))
		# Right leg
		pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-4), (self.p1+17,self.p2))
		pygame.draw.line(win, (0,0,0), (self.p1+17,self.p2), (self.p1+14,self.p2+4))
		# Eyes
		pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-8), (self.p1+6,self.p2-8))
		pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-8), (self.p1+14,self.p2-8))

	def move(self):
		self.p1 = self.p1 + self.speed

class Minion3:
	# Minion3 constructor
	def __init__(self, p1, p2):
		self.health = 1
		self.speed = 2
		self.p1 = p1
		self.p2 = p2
		self.size = 20

	def getDestroyed(self):
		self.health = 0

	def draw(self):
		if (self.health == 1):
			# Body
			pygame.draw.polygon(win, (255,255,255), [(self.p1,self.p2), (self.p1,self.p2-5), (self.p1+5,self.p2-10), (self.p1+15,self.p2-10), (self.p1+20,self.p2-5),
				(self.p1+20,self.p2), (self.p1+15,self.p2+5), (self.p1+5,self.p2+5)])
			# Left leg
			pygame.draw.line(win, (255,255,255), (self.p1+3,self.p2), (self.p1+6,self.p2+10))
			# Right leg
			pygame.draw.line(win, (255,255,255), (self.p1+17,self.p2), (self.p1+14,self.p2+10))
			# Eyes
			pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-8), (self.p1+6,self.p2-8))
			pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-8), (self.p1+14,self.p2-8))
		else:
			# Body
			pygame.draw.polygon(win, (0,0,0), [(self.p1,self.p2), (self.p1,self.p2-5), (self.p1+5,self.p2-10), (self.p1+15,self.p2-10), (self.p1+20,self.p2-5),
				(self.p1+20,self.p2), (self.p1+15,self.p2+5), (self.p1+5,self.p2+5)])
			# Left leg
			pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+6,self.p2+10))
			# Right leg
			pygame.draw.line(win, (0,0,0), (self.p1+17,self.p2), (self.p1+14,self.p2+10))
			# Eyes
			pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-8), (self.p1+6,self.p2-8))
			pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-8), (self.p1+14,self.p2-8))

	def unDraw(self):
		# Body
		pygame.draw.polygon(win, (0,0,0), [(self.p1,self.p2), (self.p1,self.p2-5), (self.p1+5,self.p2-10), (self.p1+15,self.p2-10), (self.p1+20,self.p2-5),
			(self.p1+20,self.p2), (self.p1+15,self.p2+5), (self.p1+5,self.p2+5)])
		# Left leg
		pygame.draw.line(win, (0,0,0), (self.p1+3,self.p2), (self.p1+6,self.p2+10))
		# Right leg
		pygame.draw.line(win, (0,0,0), (self.p1+17,self.p2), (self.p1+14,self.p2+10))
		# Eyes
		pygame.draw.line(win, (0,0,0), (self.p1+6,self.p2-8), (self.p1+6,self.p2-8))
		pygame.draw.line(win, (0,0,0), (self.p1+14,self.p2-8), (self.p1+14,self.p2-8))

	def move(self):
		self.p1 = self.p1 + self.speed

class Bullet:
	# Define constructor
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2
		self.length = 10

	def draw(self):
		pygame.draw.line(win, (255,255,255), (self.p1,self.p2), (self.p1,self.p2 - self.length))

	def unDraw(self):
		pygame.draw.line(win, (0,0,0),  (self.p1,self.p2), (self.p1,self.p2 - self.length*3))

	def move(self):
		self.p2 = self.p2 - self.length*3

class Player:
	# Player constructor
	def __init__(self):
		self.health = 1
		self.speed = 10
		self.p1 = 240
		self.p2 = 550
		self.size = 20

	def getDestroyed(self):
		self.health = 0

	def draw(self):
		# Body
		pygame.draw.polygon(win, (255,255,255), [(self.p1,self.p2), (self.p1,self.p2-5), (self.p1+2,self.p2-7), (self.p1+8,self.p2-7), (self.p1+10,self.p2-12),
			(self.p1+12,self.p2-7), (self.p1+18,self.p2-7), (self.p1+20,self.p2-5), (self.p1+20,self.p2)])
		# Update
		pygame.display.update()

	def unDraw(self):
		# Body
		pygame.draw.polygon(win, (0,0,0), [(self.p1,self.p2), (self.p1,self.p2-5), (self.p1+2,self.p2-7), (self.p1+8,self.p2-7), (self.p1+10,self.p2-12),
			(self.p1+12,self.p2-7), (self.p1+18,self.p2-7), (self.p1+20,self.p2-5), (self.p1+20,self.p2)])
		# Update
		pygame.display.update()

	def move(self,direction):
		self.p1 = self.p1 + direction*self.speed

	def shoot(self):
		# Draw bullet
		start_point = self.p2 -15
		bullet_speed = 2
		while (start_point > 0):
			if (start_point != self.p2 -15):
				pygame.draw.line(win, (0,0,0), (self.p1+10,self.p2-13-bullet_speed+2), (self.p1+11,self.p2-13-bullet_speed-10+2))
				pygame.display.update()

			pygame.draw.line(win, (255,255,255), (self.p1+10,self.p2-13-bullet_speed), (self.p1+10,self.p2-13-10-bullet_speed))
			bullet_speed = bullet_speed + 2
			pygame.display.update()
			start_point = self.p2-bullet_speed


# Show score on screen
def showScore(score):
	largeText = pygame.font.Font('freesansbold.ttf',20)
	if (score > 0):
		text_pr = r'<Score ' + str(score-1) + '>'
		TextSurf = largeText.render(text_pr, True, (0,0,0))
		TextRec = TextSurf.get_rect()
		win.blit(TextSurf, TextRec)
		pygame.display.update()

	
	text = r'<Score ' + str(score) + '>'
	TextSurf = largeText.render(text, True, (255,255,255))
	TextRec = TextSurf.get_rect()
	win.blit(TextSurf, TextRec)
    

# Set parameters
win_width = 480
win_height = 600

# Initialize pygame
pygame.init()
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Space invaders')

# Initialize and draw shields
sh1 = Shield(30,500)
sh2 = Shield(150,500)
sh3 = Shield(270,500)
sh4 = Shield(390,500)
sh1.draw()
sh2.draw()
sh3.draw()
sh4.draw()

# Initialize and draw minions
minion1_list = []
minion2_list = []
minion3_list = []
minion4_list = []
minion5_list = []
for i in range(10):
	minion1_list.append(Minion1(i*40 + 50, 50))
	minion1_list[i].draw()

	minion2_list.append(Minion2(i*40 + 50, 80))
	minion2_list[i].draw()

	minion3_list.append(Minion2(i*40 + 50, 110))
	minion3_list[i].draw()

	minion4_list.append(Minion3(i*40 + 50, 140))
	minion4_list[i].draw()	

	minion5_list.append(Minion3(i*40 + 50, 170))
	minion5_list[i].draw()	

# Initialize player
pl = Player()
pl.draw()

# Bullets list
bullets = []















# Main loop
score = 0
pr_score = -1
k = 1
run = True
while run:
	pygame.time.delay(100)

	# Undraw and draw all minions after applying speed
	for i in range(10):
		minion1_list[i].unDraw()
		minion1_list[i].move()
		minion1_list[i].draw()

		minion2_list[i].unDraw()
		minion2_list[i].move()
		minion2_list[i].draw()

		minion3_list[i].unDraw()
		minion3_list[i].move()
		minion3_list[i].draw()

		minion4_list[i].unDraw()
		minion4_list[i].move()
		minion4_list[i].draw()

		minion5_list[i].unDraw()
		minion5_list[i].move()
		minion5_list[i].draw()

		# If we hit an edge
		if (minion1_list[i].p1 > 460 or minion1_list[i].p1 < 20):
			for i in range(10):
				minion1_list[i].speed = minion1_list[i].speed * (-1)
				minion1_list[i].unDraw()
				minion1_list[i].p2 = minion1_list[i].p2 + 20

				minion2_list[i].speed = minion2_list[i].speed * (-1)
				minion2_list[i].unDraw()
				minion2_list[i].p2 = minion2_list[i].p2 + 20

				minion3_list[i].speed = minion3_list[i].speed * (-1)
				minion3_list[i].unDraw()
				minion3_list[i].p2 = minion3_list[i].p2 + 20

				minion4_list[i].speed = minion4_list[i].speed * (-1)
				minion4_list[i].unDraw()
				minion4_list[i].p2 = minion4_list[i].p2 + 20

				minion5_list[i].speed = minion5_list[i].speed * (-1)
				minion5_list[i].unDraw()
				minion5_list[i].p2 = minion5_list[i].p2 + 20


	# Draw bullets
	for bullet in bullets:
		bullet.unDraw()
		bullet.move()

		# Check if bullet has reached the end of the screen
		if (bullet.p2 < 0):
			bullets.remove(bullet)

		# Check if I hit a minion
 		for i in range(10):
			if (bullet.p1 > minion5_list[i].p1 and bullet.p1 < minion5_list[i].p1 + minion5_list[i].size and minion5_list[i].health == 1 and bullet.p2 < minion5_list[i].p2):
				minion5_list[i].getDestroyed()
				score = score + 1
				bullet.unDraw()
				bullets.remove(bullet)
			elif (bullet.p1 > minion4_list[i].p1 and bullet.p1 < minion4_list[i].p1 + minion4_list[i].size and minion4_list[i].health == 1 and bullet.p2 < minion4_list[i].p2):
				minion4_list[i].getDestroyed()
				score = score + 1
				bullet.unDraw()
				bullets.remove(bullet)
			elif (bullet.p1 > minion3_list[i].p1 and bullet.p1 < minion3_list[i].p1 + minion3_list[i].size and minion3_list[i].health == 1 and bullet.p2 < minion3_list[i].p2):
				minion3_list[i].getDestroyed()
				score = score + 1
				bullet.unDraw()
				bullets.remove(bullet)
			elif (bullet.p1 > minion2_list[i].p1 and bullet.p1 < minion2_list[i].p1 + minion2_list[i].size and minion2_list[i].health == 1 and bullet.p2 < minion2_list[i].p2):
				minion2_list[i].getDestroyed()
				score = score + 1
				bullet.unDraw()
				bullets.remove(bullet)
			elif (bullet.p1 > minion1_list[i].p1 and bullet.p1 < minion1_list[i].p1 + minion1_list[i].size and minion1_list[i].health == 1 and bullet.p2 < minion1_list[i].p2):
				minion1_list[i].getDestroyed()
				score = score + 1
				bullet.unDraw()
				bullets.remove(bullet)
		
		bullet.draw()

	pygame.display.update()

	# Move right/left and shoot
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_RIGHT]):
		pl.unDraw()
		pl.move(1)
		pl.draw()
	elif (keys[pygame.K_LEFT]):
		pl.unDraw()
		pl.move(-1)
		pl.draw()
	elif (keys[pygame.K_SPACE]):
		bullets.append(Bullet(pl.p1+10, pl.p2-12))
        
 
	# Show score on screen
	if (pr_score != score):
		showScore(score)
		pr_score = score


	for event in pygame.event.get():
		# Quiting event
		if (event.type == pygame.QUIT):
			run = False
