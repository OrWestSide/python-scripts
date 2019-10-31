# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style

## Functions
def printMaze(maze):
	for i in range(0, width):
		print(Fore.BLUE, '#', end=" ")
	print('\n')
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == 'c'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")
			
		print('\n')

## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 11
width = 25
maze = []

# Initialize colorama
init()

# Put walls everywhere
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# Print initial full of walls maze
# printMaze(maze)

# Randomize starting point and set it a cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'


while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]
	print(rand_wall)

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
			# Denote the new path
			maze[rand_wall[0]][rand_wall[1]] = 'c'

			# Mark the new walls
			if (rand_wall[0] != 0):
				maze[rand_wall[0]-1][rand_wall[1]] = 'w'
				walls.append([rand_wall[0]-1, rand_wall[1]])
			if (rand_wall[0] != height-1):
				maze[rand_wall[0]+1][rand_wall[1]] = 'w'
				walls.append([rand_wall[0]+1, rand_wall[1]])
			if (rand_wall[1] != 0):	
				maze[rand_wall[0]][rand_wall[1]-1] = 'w'
				walls.append([rand_wall[0], rand_wall[1]-1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
			# Denote the new path
			maze[rand_wall[0]][rand_wall[1]] = 'c'

			# Mark the new walls
			if (rand_wall[0] != 0):
				maze[rand_wall[0]-1][rand_wall[1]] = 'w'
				walls.append([rand_wall[0]-1, rand_wall[1]])
			if (rand_wall[1] != 0):
				maze[rand_wall[0]][rand_wall[1]-1] = 'w'
				walls.append([rand_wall[0], rand_wall[1]-1])
			if (rand_wall[1] != width-1):
				maze[rand_wall[0]][rand_wall[1]+1] = 'w'
				walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
			# Denote the new path
			maze[rand_wall[0]][rand_wall[1]] = 'c'

			# Mark the new walls
			if (rand_wall[0] != height-1):
				maze[rand_wall[0]+1][rand_wall[1]] = 'w'
				walls.append([rand_wall[0]+1, rand_wall[1]])
			if (rand_wall[1] != 0):
				maze[rand_wall[0]][rand_wall[1]-1] = 'w'
				walls.append([rand_wall[0], rand_wall[1]-1])
			if (rand_wall[1] != width-1):
				maze[rand_wall[0]][rand_wall[1]+1] = 'w'
				walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the right wall
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
			# Denote the new path
			maze[rand_wall[0]][rand_wall[1]] = 'c'

			# Mark the new walls
			if (rand_wall[1] != width-1):
				maze[rand_wall[0]][rand_wall[1]+1] = 'w'
				walls.append([rand_wall[0], rand_wall[1]+1])
			if (rand_wall[0] != height-1):
				maze[rand_wall[0]+1][rand_wall[1]] = 'w'
				walls.append([rand_wall[0]+1, rand_wall[1]])
			if (rand_wall[0] != 0):	
				maze[rand_wall[0]-1][rand_wall[1]] = 'w'
				walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	
	printMaze(maze)
	# time.sleep(0.5)



for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = 'w'

printMaze(maze)
