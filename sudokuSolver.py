def checkRow(board, row, value):
	for col in range(0, 9):
		if board[row][col] == value:
			return False
	return True

def checkCol(board, col, value):
	for row in range(0, 9):
		if board[row][col] == value:
			return False
	return True
	
def checkBox(board, row, col, value):
	startRow = (row // 3) * 3
	startCol = (col // 3) * 3
	for row in range(startRow, startRow + 3):
		for col in range(startCol, startCol + 3):
			if (board[row][col] == value):
				return False
	return True

def isSafeToPlace(board, row, col, value):
	if not checkRow(board, row, value):
		return False
	if not checkCol(board, col, value):
		return False
	if not checkBox(board, row, col, value):
		return False
	return True

def solveSudoku(board, row=None, col=None):
	if row == None:
		row = 0
	if col == None:
		col = 0
	if row == 9:
		return True
	if col == 9:
		return solveSudoku(board, row + 1, 0)
	for x in range(1, 10):
		if board[row][col] != -1:
			return solveSudoku(board, row, col + 1)
		if isSafeToPlace(board, row, col, x):
			board[row][col] = x
			if solveSudoku(board, row, col + 1):
				return True
			board[row][col] = -1
	return False

if __name__ == '__main__':
	example_board = [
		[3,		9,		-1,		-1,		5,		-1,		-1,		-1,		-1],
		[-1,	-1,		-1,		2,		-1,		-1,		-1,		-1,		5],
		[-1,	-1,		-1,		7,		1,		9,		-1,		8,		-1],

		[-1,	5,		-1,		-1,		6,		8,		-1,		-1,		-1],
		[2,		-1,		6,		-1,		-1,		3,		-1,		-1,		-1],
		[-1,	-1,		-1,		-1,		-1,		-1,		-1,		-1,		4],

		[5,		-1,		-1,		-1,		-1,		-1,		-1,		-1,		-1],
		[6,		7,		-1,		1,		-1,		5,		-1,		4,		-1],
		[1,		-1,		9,		-1,		-1,		-1,		2,		-1,		-1]
	]
	amount = solveSudoku(example_board)
	print(f'{amount}')
	print(example_board)