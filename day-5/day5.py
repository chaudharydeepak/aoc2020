file1 = open('input.txt', 'r') 
Lines = file1.readlines() 


highest = 0



def determine_row(line):
	row_range = [0, 127]

	for i in range(6):
		if line[i] == 'F':
			row_range[1] = (row_range[0] + row_range[1]) // 2
		else:
			row_range[0] = (row_range[0] + row_range[1] + 1) // 2
	
	if line[6] == 'F':
		return row_range[0]
	else:
		return row_range[1]

def determine_column(line):
	col_range = [0,  7]

	for i in range(7, 10):
		if line[i] == 'L':
			col_range[1] = (col_range[0] + col_range[1]) // 2
		else:
			col_range[0] = (col_range[0] + col_range[1] + 1) // 2
	if line[6] == 'L':
		return col_range[0]
	else:
		return col_range[1]

seats = [0] * 128 * 8

for line in Lines:
	# Part 1
	row = determine_row(line)

	column = determine_column(line)

	seat_id = row * 8 + column

	if seat_id > highest:
		highest = seat_id

	# Part 2
	seats[seat_id] = 1

print(highest)

print(seats)

# Part 2
for i in range(128 * 8):
	if (not seats[i]):
		print(i)


