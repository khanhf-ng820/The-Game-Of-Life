import pygame, math
from sys import exit


width, height = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway\'s Game of Life")
clock = pygame.time.Clock()

size = 20
cols, rows = width//size, height//size
grid = [[0 for i in range(cols+2)] for j in range(rows+2)]
done_init = False

def notter(b):
	if b == 0:
		return 1
	else:
		return 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if (not done_init) and event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			cellx = math.ceil(x/size)
			celly = math.ceil(y/size)
			grid[celly][cellx] = notter(grid[celly][cellx])
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				done_init = True
				if done_init:
					print("Done initializing!")

	# Processing next gen
	nextgrid = [[0 for i in range(cols+2)] for j in range(rows+2)]
	
	if done_init:
		for col in range(1, cols+1):
			for row in range(1, rows+1):
				neighbors = [
					grid[row-1][col-1],
					grid[row-1][col],
					grid[row-1][col+1],
					grid[row][col-1],
					grid[row][col+1],
					grid[row+1][col-1],
					grid[row+1][col],
					grid[row+1][col+1],
				]
				alive_neighbors = sum(neighbors)
				
				# Count live neighbors
				if grid[row][col] == 0 and alive_neighbors == 3:
					nextgrid[row][col] = 1
				elif grid[row][col] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
					nextgrid[row][col] = 0
				else:
					nextgrid[row][col] = grid[row][col]
		grid = nextgrid

	# Drawing
	screen.fill(BLACK)
	for col in range(cols):
		for row in range(rows):
			if grid[row+1][col+1] == 1:
				CELLCOLOR = YELLOW
			else:
				CELLCOLOR = GREY
			pygame.draw.rect(screen, BLACK, (col*size, row*size, size, size), 0)
			pygame.draw.rect(screen, CELLCOLOR, (col*size+1, row*size+1, size-1, size-1), 0)

	pygame.display.update()
	clock.tick(60)
