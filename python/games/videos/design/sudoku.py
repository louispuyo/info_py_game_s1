import pygame
import sys
import copy

pygame.init()
width = 450
height = 450

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SUDOCU')
clock = pygame.time.Clock()

def reference(index):
	if index == 1:
		return ([[0, 0, 0, 0, 6, 0, 7, 0, 0], 
				[0, 5, 9, 0, 0, 0, 0, 0, 0],
				[0, 1, 0, 2, 0, 0, 0, 0, 0],
				[0, 0, 0, 1, 0, 0, 0, 0, 0],
				[6, 0, 0, 5, 0, 0, 0, 0, 0],
				[3, 0, 0, 0, 0, 0, 4, 6, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 9, 1],
				[8, 0, 0, 7, 4, 0, 0, 0, 0]])

	elif index == 2:
		return ([[5, 0, 4, 8, 0, 0, 0, 2, 0], 
				[7, 0, 0, 0, 9, 6, 1, 0, 0],
				[0, 3, 0, 7, 0, 0, 6, 0, 0],
				[9, 2, 0, 0, 4, 8, 3, 0, 0],
				[8, 4, 0, 0, 0, 0, 0, 1, 2],
				[0, 0, 3, 1, 7, 0, 0, 4, 9],
				[0, 0, 6, 0, 0, 4, 0, 5, 0],
				[0, 0, 5, 3, 6, 0, 0, 0, 8],
				[0, 1, 0, 0, 0, 7, 2, 0, 3]])

	elif index == 3:
		return ([[4, 0, 3, 0, 0, 2, 0, 0, 0], 
				[5, 0, 0, 0, 6, 0, 1, 2, 0],
				[9, 0, 0, 0, 0, 0, 0, 0, 4],
				[0, 0, 8, 0, 7, 0, 0, 0, 0],
				[0, 0, 0, 2, 0, 3, 0, 0, 8],
				[0, 3, 6, 0, 0, 0, 7, 0, 0],
				[0, 7, 0, 9, 2, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 5, 0, 9, 6],
				[0, 0, 0, 8, 0, 4, 5, 0, 0]])

	elif index == 4:
		return ([[7, 0, 9, 0, 0, 0, 0, 0, 0],
				[0, 0, 4, 0, 3, 5, 0, 0, 0],
				[0, 1, 0, 0, 0, 0, 0, 0, 9],
				[3, 4, 6, 0, 0, 0, 0, 2, 0],
				[9, 5, 7, 2, 0, 0, 1, 4, 3],
				[0, 0, 8, 4, 0, 3, 0, 0, 0],
				[0, 7, 0, 0, 0, 2, 0, 8, 0],
				[0, 0, 0, 6, 5, 0, 7, 0, 0],
				[0, 0, 1, 0, 0, 9, 5, 3, 0]])

	elif index == 5:
		return ([[5, 3, 0, 0, 7, 0, 0, 0, 0],
				[6, 0, 0, 1, 9, 5, 0, 0, 0],
				[0, 9, 8, 0, 0, 0, 0, 6, 0],
				[8, 0, 0, 0, 6, 0, 0, 0, 3],
				[4, 0, 0, 8, 0, 3, 0, 0, 1],
				[7, 0, 0, 0, 2, 0, 0, 0, 6],
				[0, 6, 0, 0, 0, 0, 2, 8, 0],
				[0, 0, 0, 4, 1, 9, 0, 0, 5],
				[0, 0, 0, 0, 8, 0, 0, 7, 9]])

	elif index == 6:
		return ([[0, 0, 5, 3, 0, 0, 0, 0, 0],
				[8, 0, 0, 0, 0, 0, 0, 2, 0],
				[0, 7, 0, 0, 1, 0, 5, 0, 0],
				[4, 0, 0, 0, 0, 5, 3, 0, 0],
				[0, 1, 0, 0, 7, 0, 0, 0, 6],
				[0, 0, 3, 2, 0, 0, 0, 8, 0],
				[0, 6, 0, 5, 0, 0, 0, 0, 9],
				[0, 0, 4, 0, 0, 0, 0, 3, 0],
				[0, 0, 0, 0, 0, 9, 7, 0, 0]])

	elif index == 7:
		return ([[0, 0, 6, 0, 0, 4, 0, 5, 0],
				[0, 0, 5, 3, 6, 0, 0, 0, 8],
				[0, 1, 0, 0, 0, 7, 2, 0, 3],
				[5, 0, 4, 8, 0, 0, 0, 2, 0], 
				[7, 0, 0, 0, 9, 6, 1, 0, 0],
				[0, 3, 0, 7, 0, 0, 6, 0, 0],
				[9, 2, 0, 0, 4, 8, 3, 0, 0],
				[8, 4, 0, 0, 0, 0, 0, 1, 2],
				[0, 0, 3, 1, 7, 0, 0, 4, 9]])

	elif index == 8:
		return ([[0, 0, 8, 0, 7, 0, 0, 0, 0],
				[0, 0, 0, 2, 0, 3, 0, 0, 8],
				[0, 3, 6, 0, 0, 0, 7, 0, 0],
				[0, 7, 0, 9, 2, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 5, 0, 9, 6],
				[0, 0, 0, 8, 0, 4, 5, 0, 0],
				[4, 0, 3, 0, 0, 2, 0, 0, 0], 
				[5, 0, 0, 0, 6, 0, 1, 2, 0],
				[9, 0, 0, 0, 0, 0, 0, 0, 4]])

def draw_field():
	pygame.draw.line(screen, (0, 0, 0), (50, 0), (50, 500), 1)
	pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 500), 1)
	pygame.draw.line(screen, (0, 0, 0), (150, 0), (150, 500), 3)
	pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 500), 1)
	pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 500), 1)
	pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 500), 3)
	pygame.draw.line(screen, (0, 0, 0), (350, 0), (350, 500), 1)
	pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 500), 1)

	pygame.draw.line(screen, (0, 0, 0), (0, 50), (500, 50), 1)
	pygame.draw.line(screen, (0, 0, 0), (0, 100), (500, 100), 1)
	pygame.draw.line(screen, (0, 0, 0), (0, 150), (500, 150), 3)
	pygame.draw.line(screen, (0, 0, 0), (0, 200), (500, 200), 1)
	pygame.draw.line(screen, (0, 0, 0), (0, 250), (500, 250), 1)
	pygame.draw.line(screen, (0, 0, 0), (0, 300), (500, 300), 3)
	pygame.draw.line(screen, (0, 0, 0), (0, 350), (500, 350), 1)
	pygame.draw.line(screen, (0, 0, 0), (0, 400), (500, 400), 1)

def get_pos(pos_x, pos_y):
	b = 0
	for i in range(50, 500, 50):
		if pos_y <= i and pos_y	>= b:
			pos_y = i / 50
			break
		else:
			b += 50	

	a = 0
	for j in range(50, 500, 50):
		if pos_x <= j and pos_x >= a:
			pos_x = j / 50
			break 
		else:
			a += 50

	return(pos_x, pos_y)
		
field = [[0] * 9 for i in range(9)]

def fill_field(field, cell):
	if field[int(cell[0]) - 1][int(cell[1]) - 1] != 0:
		if pygame.key.get_pressed()[pygame.K_DELETE]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 0

	if field[int(cell[0]) - 1][int(cell[1]) - 1] == 0:
		if pygame.key.get_pressed()[pygame.K_1]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 1

		elif pygame.key.get_pressed()[pygame.K_2]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 2

		elif pygame.key.get_pressed()[pygame.K_3]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 3

		elif pygame.key.get_pressed()[pygame.K_4]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 4

		elif pygame.key.get_pressed()[pygame.K_5]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 5

		elif pygame.key.get_pressed()[pygame.K_6]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 6

		elif pygame.key.get_pressed()[pygame.K_7]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 7

		elif pygame.key.get_pressed()[pygame.K_8]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 8

		elif pygame.key.get_pressed()[pygame.K_9]:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = 9

	return(field[int(cell[0]) - 1][int(cell[1]) - 1])

def error(index):
	if index == 1:
		pygame.draw.rect(screen, (255, 0, 0), ((0, 0), (450, 450)))

	pygame.draw.line(screen, (0, 0, 0), (10, 150), (80, 150), 5)
	pygame.draw.line(screen, (0, 0, 0), (10, 150), (10, 300), 5)
	pygame.draw.line(screen, (0, 0, 0), (10, 300), (80, 300), 5)
	pygame.draw.line(screen, (0, 0, 0), (10, 225), (80, 225), 5)

	pygame.draw.line(screen, (0, 0, 0), (100, 150), (170, 150), 5)
	pygame.draw.line(screen, (0, 0, 0), (100, 150), (100, 300), 5)

	pygame.draw.line(screen, (0, 0, 0), (190, 150), (260, 150), 5)
	pygame.draw.line(screen, (0, 0, 0), (190, 150), (190, 300), 5)

	pygame.draw.line(screen, (0, 0, 0), (280, 150), (350, 150), 5)
	pygame.draw.line(screen, (0, 0, 0), (280, 300), (350, 300), 5)
	pygame.draw.line(screen, (0, 0, 0), (280, 150), (280, 300), 5)
	pygame.draw.line(screen, (0, 0, 0), (350, 150), (350, 300), 5)

	pygame.draw.line(screen, (0, 0, 0), (370, 150), (440, 150), 5)
	pygame.draw.line(screen, (0, 0, 0), (370, 150), (370, 300), 5)
	pygame.display.flip()
	pygame.time.delay(1000)
	return

def numbers(field):
	for i in range(9):
		for j in range(9):
			if field[i][j] == 1:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 25, j * 50 + 7), (i * 50 + 25, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 25, j * 50 + 7), (i * 50 + 20, j * 50 + 15), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 20, (j + 1) * 50 - 7), (i * 50 + 30, (j + 1) * 50 - 7), 3)
			if field[i][j] == 2:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 15, j * 50 + 7), (i * 50 + 35, j * 50 + 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, j * 50 + 7), (i * 50 + 35, (j + 1) * 50 - 28), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, (j + 1) * 50 - 28), (i * 50 + 13, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 13, (j + 1) * 50 - 7), (i * 50 + 37, (j + 1) * 50 - 7), 3)
			if field[i][j] == 3:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 15, j * 50 + 7), (i * 50 + 35, j * 50 + 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, j * 50 + 7), (i * 50 + 30, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 30, (j + 1) * 50 - 25), (i * 50 + 35, (j + 1) * 50 - 22), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, (j + 1) * 50 - 22), (i * 50 + 35, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 15, (j + 1) * 50 - 7), (i * 50 + 35, (j + 1) * 50 - 7), 3)
			if field[i][j] == 4:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, j * 50 + 7), (i * 50 + 35, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, j * 50 + 25), (i * 50 + 15, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 18, j * 50 + 7), (i * 50 + 15, (j + 1) * 50 - 25), 3)
			if field[i][j] == 5:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 33, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 17, j * 50 + 43), (i * 50 + 33, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 20, j * 50 + 7), (i * 50 + 33, j * 50 + 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 20, j * 50 + 7), (i * 50 + 17, (j + 1) * 50 - 25), 3)
			if field[i][j] == 6:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 28, j * 50 + 7), (i * 50 + 17, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 43), (i * 50 + 17, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 33, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 17, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 7), 3)
			if field[i][j] == 7:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 15, j * 50 + 7), (i * 50 + 35, j * 50 + 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 35, j * 50 + 7), (i * 50 + 25, j * 50 + 43), 3)
			if field[i][j] == 8:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 43), (i * 50 + 17, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 33, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 17, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 7), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 32, j * 50 + 8), (i * 50 + 18, j * 50 + 8), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 32, j * 50 + 25), (i * 50 + 32, (j + 1) * 50 - 42), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 18, j * 50 + 25), (i * 50 + 18, (j + 1) * 50 - 42), 3)
			if field[i][j] == 9:
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 25), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 7), (i * 50 + 17, (j + 1) * 50 - 43), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 33, (j + 1) * 50 - 43), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 17, j * 50 + 25), (i * 50 + 17, (j + 1) * 50 - 43), 3)
				pygame.draw.line(screen, (50, 50, 0), (i * 50 + 33, j * 50 + 25), (i * 50 + 23, (j + 1) * 50 - 7), 3)

class SudokuSolver:
	def solve(puzzle):
		solution = copy.deepcopy(puzzle)
		if SudokuSolver.solveHelper(solution):
			return solution
		return None

	def solveHelper(solution):
		minPossibleValueCountCell = None

		while True:
			minPossibleValueCountCell = None

			for rowIndex in range(9):
				for columnIndex in range(9):
					if solution[rowIndex][columnIndex] != 0:
						continue

					possibleValues = SudokuSolver.findPossibleValues(rowIndex, columnIndex, solution)
					possibleValueCount = len(possibleValues)
					if possibleValueCount == 0:
						return False

					if possibleValueCount == 1:
						solution[rowIndex][columnIndex] = possibleValues.pop()

					if not minPossibleValueCountCell or possibleValueCount < len(minPossibleValueCountCell[1]):
						minPossibleValueCountCell = ((rowIndex, columnIndex), possibleValues)

			if not minPossibleValueCountCell:
				return True

			elif 1 < len(minPossibleValueCountCell[1]):
				break

		r, c = minPossibleValueCountCell[0]

		for v in minPossibleValueCountCell[1]:
			solutionCopy = copy.deepcopy( solution )
			solutionCopy[r][c] = v

			if SudokuSolver.solveHelper(solutionCopy):
				for r in range(9):
					for c in range(9):
						solution[r][c] = solutionCopy[r][c]
				return True
		return False

	def findPossibleValues(rowIndex, columnIndex, puzzle):

		values = {v for v in range(1, 10)}

		values -= SudokuSolver.getRowValues(rowIndex, puzzle)
		values -= SudokuSolver.getColumnValues(columnIndex, puzzle)
		values -= SudokuSolver.getBlockValues(rowIndex, columnIndex, puzzle)
		return values

	def getRowValues(rowIndex, puzzle):
		return set(puzzle[rowIndex][:])

	def getColumnValues(columnIndex, puzzle):
		return {puzzle[r][columnIndex] for r in range(9)}

	def getBlockValues(rowIndex, columnIndex, puzzle):
		blockRowStart = 3 * (rowIndex // 3)
		blockColumnStart = 3 * (columnIndex // 3)
		return {puzzle[blockRowStart + r][blockColumnStart + c] for r in range(3) for c in range(3)}

	def CheckPuzzle(puzzle):
		set_of_val = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
		for i in range(9):
			row_val = SudokuSolver.getRowValues(i, puzzle)
			if row_val != set_of_val:
				return False
			col_val = SudokuSolver.getColumnValues(i, puzzle)
			if col_val != set_of_val:
				return False
			block_val = SudokuSolver.getBlockValues(i, i, puzzle)
			if block_val != set_of_val:
				return False
		return True


print('To start playing press a key from a to h to choose one of eight fields')
print('To insert your own game hold mouse upon needed cell and press a digit on the keyboard')
print('To delete specific number hold mouse and press DELETE')
print('For solution press SPACE')
print('To clear field prsess END')
print('To get a clue press 0 upon needed cell')

while True:
	dt = clock.tick(50) / 1000.0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


	screen.fill((255, 255, 200))
	pos = pygame.mouse.get_pos()
	pos_x, pos_y = pos[0], pos[1]

	cell = get_pos(int(pos_x), int(pos_y))

	pygame.draw.rect(screen, (191, 239, 255), ((cell[0]-1)*50, (cell[1]-1)*50, 50, 50), 50)

	if pygame.key.get_pressed()[pygame.K_a]:
		field = reference(1)

	if pygame.key.get_pressed()[pygame.K_b]:
		field = reference(2)

	if pygame.key.get_pressed()[pygame.K_c]:
		field = reference(3)

	if pygame.key.get_pressed()[pygame.K_d]:
		field = reference(4)

	if pygame.key.get_pressed()[pygame.K_e]:
		field = reference(5)

	if pygame.key.get_pressed()[pygame.K_f]:
		field = reference(6)

	if pygame.key.get_pressed()[pygame.K_g]:
		field = reference(5)

	if pygame.key.get_pressed()[pygame.K_h]:
		field = reference(6)

	fill_field(field, cell)

	if pygame.key.get_pressed()[pygame.K_END]:
		field = [[0] * 9 for i in range(9)]	

	draw_field()

	numbers(field)

	if pygame.key.get_pressed()[pygame.K_0]:
		solution = SudokuSolver.solve(field)
		if solution:
			field[int(cell[0]) - 1][int(cell[1]) - 1] = solution[int(cell[0]) - 1][int(cell[1]) - 1]
		else:
			error(1)
			print('Error in the field - no solution')

	if pygame.key.get_pressed()[pygame.K_SPACE]:
		solution = SudokuSolver.solve(field)
		if solution and SudokuSolver.CheckPuzzle(solution):
			field = solution
		else:
			error(1)
			print('Error in the field - no solution')

	pygame.display.flip()