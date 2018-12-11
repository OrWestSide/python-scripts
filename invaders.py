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
		self.speed = 1
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
		self.speed = 1
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
		self.speed = 1
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

# Define function that draws the bullet (we are going to use this a lot)
def drawBullet(start_point, end_point, b_speed):
	# Bullet speed & other params
	bullet_speed = b_speed
	first = True
	# While target not hit
	while (start_point > end_point):
		if (first == False):
			pygame.draw.line(win, (0,0,0), (pl.p1+10,pl.p2-13-bullet_speed+b_speed), (pl.p1+10,pl.p2-13-bullet_speed-10+b_speed))
			pygame.display.update()
		pygame.draw.line(win, (255,255,255), (pl.p1+10,pl.p2-13-bullet_speed), (pl.p1+10,pl.p2-13-10-bullet_speed))
		bullet_speed = bullet_speed + b_speed
		pygame.display.update()
		start_point = start_point - 1*b_speed	
		first = False
	pygame.draw.line(win, (0,0,0), (pl.p1+10,pl.p2-13-bullet_speed+2), (pl.p1+10,pl.p2-13-bullet_speed-10))
	pygame.display.update()	

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

		if (minion1_list[i].p1 > 460 or minion1_list[i].p1 < 20):
			for i in range(10):
				minion1_list[i].speed = minion1_list[i].speed * (-1)
				minion2_list[i].speed = minion2_list[i].speed * (-1)
				minion3_list[i].speed = minion3_list[i].speed * (-1)
				minion4_list[i].speed = minion4_list[i].speed * (-1)
				minion5_list[i].speed = minion5_list[i].speed * (-1)

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

		# Check if shield is hit
		if (pl.p1 + 10 > 30 and pl.p1 + 10 < 30 + sh1.size and sh1.health > 0):
			drawBullet(pl.p2-15, 500, 1)		
			sh1.getHit()
			sh1.draw()
		elif (pl.p1 + 10 > 150 and pl.p1 + 10 < 150 + sh2.size and sh2.health > 0):
			drawBullet(pl.p2-15, 500, 1)
			sh2.getHit()
			sh2.draw()
		elif (pl.p1 + 10 > 270 and pl.p1 + 10 < 270 + sh3.size and sh3.health > 0):
			drawBullet(pl.p2-15, 500, 1)
			sh3.getHit()
			sh3.draw()
		elif (pl.p1 + 10 > 390 and pl.p1 + 10 < 390 + sh4.size and sh4.health > 0):
			drawBullet(pl.p2-15, 500, 1)		
			sh4.getHit()
			sh4.draw()
		else:
			# If a shield is not hit, check if a minion is hit
			pos = -1
			for i in range(10):
				if (pl.p1 + 10 > minion5_list[i].p1 and pl.p1 + 10 < minion5_list[i].p1 + minion5_list[i].size):
					pos = i
					break
			
			# We now have the column the bullet should hit. Kill the first one you see alive
			if (pos != -1):
				if (minion5_list[pos].health == 1):
					drawBullet(pl.p2-15, minion5_list[pos].p2, 5)
					score = score + 1
					minion5_list[pos].getDestroyed()
					minion5_list[pos].draw()
				elif (minion4_list[pos].health == 1):
					drawBullet(pl.p2-15, minion4_list[pos].p2, 5)
					score = score + 1
					minion4_list[pos].getDestroyed()
					minion4_list[pos].draw()
				elif (minion3_list[pos].health == 1):
					drawBullet(pl.p2-15, minion3_list[pos].p2, 5)
					score = score + 1
					minion3_list[pos].getDestroyed()
					minion3_list[pos].draw()
				elif (minion2_list[pos].health == 1):
					drawBullet(pl.p2-15, minion2_list[pos].p2, 5)
					score = score + 1
					minion2_list[pos].getDestroyed()
					minion2_list[pos].draw()
				else:
					for i in range(10):
						# If the four first rows are destoyed, check for first row points
						if (pl.p1 + 10 > minion1_list[i].p1 and pl.p1 + 10 < minion1_list[i].p1 + minion1_list[i].size and minion1_list[i].health == 1):
							score = score + 1
							drawBullet(pl.p2-15, minion1_list[pos].p2, 5)
							minion1_list[i].getDestroyed()
							minion1_list[i].draw()
							break
			else:
				# If nothing is hit...
				pl.shoot()
 
	# Show score on screen
	if (pr_score != score):
		showScore(score)
		pr_score = score


	for event in pygame.event.get():
		# Quiting event
		if (event.type == pygame.QUIT):
			run = False