import copy 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
for i in range(len(Lines)):
	Lines[i] = list(Lines[i])


width = len(Lines[0]) - 1 # account for newline
height = len(Lines)

# # part 1
# # returns true if adjacent cells are open, false otherwise
# def check_adjacent(board, row, col):

# 	if row == 0:
# 		top = 3
# 	else:
# 		top = 3 - board[row -1][max(col-1,0):col+2].count("#")

# 	if col == 0:
# 		left = 1
# 	elif board[row][col-1] != "#":
# 		left = 1
# 	else:
# 		left = 0

# 	if col == width - 1:
# 		right = 1
# 	elif board[row][col+1] != "#":
# 		right = 1
# 	else:
# 		right = 0

# 	if row == height - 1:
# 		bottom = 3
# 	else:
# 		bottom = 3 - board[row + 1][max(col-1,0):col+2].count("#")
# 	return top + left + right + bottom


def check_adjacent(board, row, col):
	free = 8
	slopes = [-1, 0 ,1]
	for vert in slopes:
		for horiz in slopes:
			if vert == 0 and horiz == 0:
				continue
			x = col + horiz
			y = row + vert
			while x in range(width) and y in range(height):
				if board[y][x] == "#":
					free -= 1
					break
				if board[y][x] == "L":
					break
				x += horiz
				y += vert
	return free


def perform_round(prev_board):
	new_board = copy.deepcopy(prev_board)
	changes = 0
	for row in range(height):
		for col in range(width):

			# print(row, col, check_adjacent(prev_board, row, col))
			if prev_board[row][col] == "L" and check_adjacent(prev_board, row, col) == 8:
				new_board[row][col] = "#"
				changes += 1
			if prev_board[row][col] == "#" and check_adjacent(prev_board, row, col) <= 3:
				new_board[row][col] = "L"
				changes += 1
	# for line in new_board:
	# 	print(''.join(map(str, line))[:-1])
	# print(changes)
	return new_board, changes

def iterate_until_stasis():
	changes = -1
	new_board = Lines

	while (changes != 0):
		temps = []
		temp, changes = perform_round(new_board)
		new_board = copy.deepcopy(temp)

	return new_board

def count_occupied(board):
	occupied = 0
	for line in board:
		occupied += line.count("#")
	return occupied


# print(check_adjacent(Lines,0,3))
print(count_occupied(iterate_until_stasis()))