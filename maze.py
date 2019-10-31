# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time

## Functions
def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			print(maze[i][j], end=" ")
		print('\n')

## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 11
width = 17
maze = []

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


while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]


	nearby_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		nearby_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		nearby_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		nearby_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		nearby_cells += 1

	if (nearby_cells < 2):
		maze[rand_wall[0]][rand_wall[1]] = 'c'
		if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
			walls.append([rand_wall[0]-1, rand_wall[1]])
		if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
			walls.append([rand_wall[0], rand_wall[1]-1])
		if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
			walls.append([rand_wall[0], rand_wall[1]+1])
		if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
			walls.append([rand_wall[0]+1, rand_wall[1]])

	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
			break

	printMaze(maze)
	time.sleep(0.5)
