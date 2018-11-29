import pygame
import numpy

# Set parameters
win_width = 700
win_height = 400
values = numpy.random.rand(1,win_width)*win_height 

# Initialize pygame
pygame.init()
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Bubble Sort Visualization')

# Create my loop
run = True
done = False
swaps = 0
while run:
	pygame.time.delay(100)

	if (done == False):
		for i in range(0, len(values[0])-1):
			for j in range(0,len(values[0])-i-1):
				if (values[0][j] < values[0][j+1]):
					tmp = values[0][j]
					values[0][j] = values[0][j+1]
					values[0][j+1] = tmp
					swaps = swaps + 1
			
			win.fill((0,0,0))
			# Draw lines
			for i in range(0,win_width):
				pygame.draw.line(win, (255, 255, 255), (i, win_height), (i, values[0][i]))

			pygame.display.update()

		print('\nNumber of swaps made: ' + str(swaps))
		done = True
	
	# If user presses X, quit the loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False