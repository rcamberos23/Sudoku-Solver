board = [

	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]

]

def solve(board):

	find = find_empty(board)
	if find:
		row, col = find
	else:
		return True

	for i in range(1,10):
		if valid(board, (row, col), i):
			board[row][col] = i
			if solve(board):
				return True
			board[row][col] = 0
	return False

def valid(board, pos, num):
	for i in range(0, len(board)):
		if board[pos[0]][i] == num and pos[1] != i:
			return False
	for i in range(0, len(board)):
		if board[i][pos[1]] == num and pos[1] != i:
			return False

	boardx_x = pos[1]//3
	boardx_y = pos[0]//3
	for i in range(boardx_y*3, boardx_y*3 + 3):
		for j in range(boardx_x*3, boardx_x*3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False
	return True

def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None

def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("---------------")
		for j in range(len(board[0])):
			if j % 3 == 0:
				print(" | ", end="")
			if j == 8:
				print(board[i][j], end = "\n")
			else:
				print(str(board[i][j]) + " ", end="")

print("Starting with this")
print_board(board)
print("Solving board")
solve(board)
print("Solved board below")
print_board(board)