file1 = open('input2.txt', 'r') 
Lines = file1.readlines() 


x = 0
y = 0

waypoint_x = 10
waypoint_y = 1


direction = 90

# part 1
# for line in Lines:
# 	if line[0] == "F":
# 		# facing north
# 		if direction == 0:
# 			y += int(line[1:-1])
# 		# facing east
# 		elif direction == 90:
# 			x += int(line[1:-1])
# 		# facing south
# 		elif direction == 180:
# 			y -= int(line[1:-1])
# 		# facing west
# 		else:
# 			x -= int(line[1:-1])
# 	if line[0] == "N":
# 		y += int(line[1:-1])
# 	if line[0] == "E":
# 		x += int(line[1:-1])
# 	if line[0] == "S":
# 		y -= int(line[1:-1])
# 	if line[0] == "W":
# 		x -= int(line[1:-1])
# 	if line[0] == "L":
# 		direction -= int(line[1:-1])
# 		direction = direction % 360
# 	if line[0] == "R":
# 		direction += int(line[1:-1])
# 		direction = direction % 360


def move_to_waypoint():
	global x
	global y
	x += waypoint_x
	y += waypoint_y

def rotate_waypoint(amount):
	global direction
	global waypoint_x
	global waypoint_y
	direction += int(amount)
	direction = direction % 360


	times = int((amount % 360) / 90)

	for i in range(times):
		temp = waypoint_x
		waypoint_x = waypoint_y
		waypoint_y = -1 * temp

for line in Lines:
	if line[0] == "F":
		for i in range(int(line[1:-1])):
			move_to_waypoint()
	if line[0] == "N":
		waypoint_y += int(line[1:-1])
	if line[0] == "E":
		waypoint_x += int(line[1:-1])
	if line[0] == "S":
		waypoint_y -= int(line[1:-1])
	if line[0] == "W":
		waypoint_x -= int(line[1:-1])
	if line[0] == "L":
		rotate_waypoint(-1 * int(line[1:-1]))
	if line[0] == "R":
		rotate_waypoint(int(line[1:-1]))



print(abs(x) + abs(y))