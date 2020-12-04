file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

down = 1
over = 3

line_total = len(Lines)
# -1 to account for newlines
line_length = len(Lines[0]) - 1

def trees_with_slope(down, over):
	x = 0
	y = 0
	num_trees = 0
	while (y < line_total):
		if (Lines[y][x] == "#"):
			num_trees += 1
		x = (x + over) % line_length
		y += down
	return num_trees

print(trees_with_slope(1,1) * trees_with_slope(1,3) *trees_with_slope(1,5) *trees_with_slope(1,7) *trees_with_slope(2,1))