# line = [0] * 3
# board = line * 3
board = [[0,0,0],[0,0,0],[0,0,0]]


def printLine(input):
	i = 0
	# print(" ")
	while i < 3:
		if input[i] == 1:
			print("X", end='')
		elif input[i] == 2:
			print("O", end='')
		else:
			print(" ", end='')
		if i != 2:
			print(" | ", end="")
		i = i + 1
	print(" ")
	print("----------")

def printBoard():
	print("----------")
	printLine(board[0])
	printLine(board[1])
	printLine(board[2])
	# print(board[0])
	# print(board[1])
	# print(board[2])
	




def check_user_input_row(input):
	try:
		row = int(input[1])
		if row < 0 or row > 2:
			print("Input row is < 0 or > 2")
			return -1
		return row
	except ValueError:
		print("Input row is not integer")
		return -1

def check_user_input_col(input):
	try:
		col = int(input[0])
		if col < 0 or col > 2:
			print("Input for col is < 0 or > 2")
			return -1
		return col
	except ValueError:
		print("Input col is not integer")
		return -1

def check_line_win(line):
	if line[0] == 1 and line [1] == 1 and line[2] == 1:
		return 1
	elif line[0] == 2 and line [1] == 2 and line[2] == 2:
		return 2
	return 0
def check_row_win(row):
	if board[0][row] == 1 and board[1][row] == 1 and board[2][row] == 1:
		return 1
	elif board[0][row] == 2 and board[1][row] == 2 and board[2][row] == 2:
		return 2
	return 0
def check_diagonal_win(case):
	if case == 0:
		if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
			return 1
		elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
			return 2
		return 0
	else:
		if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
			return 1
		elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
			return 2
		return 0
	return 0

def check_line_full(row):
	if board[row][0] != 0 and board[row][1] != 0 and board[row][2] != 0:
		return True
	return False

def check_draw():
	if check_line_full(0) == True and check_line_full(1) == True and check_line_full(2) == True:
		return 1
	return 0


def check_if_end():
	res = check_line_win(board[0])
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_line_win(board[1])
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_line_win(board[2])
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_row_win(0)
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_row_win(1)
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_row_win(2)
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_diagonal_win(0)
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_diagonal_win(1)
	if res == 1 or res == 2:
		print("Player Nr. ", res, " won!")
		return res
	res = check_draw()
	if res == 1:
		print("Game is drawed!")
	return res

turn = 1
gameover = False

while gameover == False:
	printBoard()
	val = input("Enter your value: ")
	if len(val) < 2 or len(val) > 2:
		print("Too much or too little Input")
		continue
	row = check_user_input_row(val)
	if row == -1:
		continue
	col = check_user_input_col(val)
	if col == -1:
		continue
	if board[col][row] != 0:
		print("This position is already taken")
		continue
	board[col][row] = turn
	if turn == 1:
		turn = 2
	else:
		turn = 1
	res = check_if_end()
	print("res = ", res)
	if res != 0:
		gameover = True