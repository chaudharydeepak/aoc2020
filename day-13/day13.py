import sys
def part_1():
	file1 = open('input.txt', 'r') 
	Lines = file1.readlines() 

	timestamp = int(Lines[0])

	buses = Lines[1].split(",")

	min_wait_time = sys.maxsize * 2 + 1
	min_bus = -1
	for i in range(len(buses)):
		try:
			bus_id = int(buses[i])
			if timestamp % bus_id == 0:
				return 0
			division = timestamp / bus_id
			wait_time = ((division + 1) % timestamp) * bus_id
			if wait_time  < min_wait_time:
				min_wait_time = wait_time
				min_bus = bus_id
		except Exception as e:
			continue
	return (min_wait_time - timestamp) * min_bus

# I got some help from the folliwng reddit post:
# https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/
def part_2():
	file1 = open('input.txt', 'r') 
	Lines = file1.readlines() 

	buses = Lines[1].split(",")

	spacing = []
	for i in range(len(buses)):
		if buses[i] != "x":
			spacing.append(i)

	# amount to increment time forward. we start with the id of the first bus
	increment = int(buses[spacing[0]])

	time = 0
	for i in range(1, len(spacing)):
		while True:
			time += increment
			cur_bus_id = int(buses[spacing[i]])
			prev_bus_id = int(buses[spacing[i - 1]])
			# check when the time aligns between the current bus, its spacing, and the previous bus
			if ((time + spacing[i - 1]) % prev_bus_id == 0) and ((time + spacing[i]) % cur_bus_id == 0):
				# we know that every subsequent timestamp at which the current bus can depart AND align with all the
				# previously departed buses with the right spacing will be a multiple of the current bus's ID.
				# So, our increment can be multiplied by the ID of the current bus
				increment *= cur_bus_id
				break
	return time

print(part_2())