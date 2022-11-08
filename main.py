# line = [0] * 3
# board = line * 3
board = [[0,0,0],[0,0,0],[0,0,0]]

def printLine(input):
	i = 0
	# print(" ")
	while i < 3:
		if input[i] == 1:
			# print("X", end='')
			print("1", end='')
		elif input[i] == 2:
			# print("O, end='')
			print("2", end='')
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

def check_line_win(x):
	if board[x][0] == board[x][1] == 1 and board[x][0] == board[x][2]:
		return board[x][0]
	if board[0][x] == board[1][x] == 1 and board[0][x] == board[2][x]:
		return board[0][x]
	return 0

def check_diagonal_win():
	if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
		return board[0][0]
	if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
		return board[0][2]
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
	i = 0
	while i < 3:
		res = check_line_win(i)
		if res != 0:
			print("Player Nr. ", res, " won!")
			return res
		i = i + 1
	res = check_diagonal_win()
	if res != 0:
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