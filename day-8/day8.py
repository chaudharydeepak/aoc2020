file1 = open('input.txt', 'r') 
Lines = file1.readlines() 


def execute(switch_nop, switch_jmp):
	execution_tracker = [0] * len(Lines)

	accumulator = 0

	line_num = 0
	while True:


		if line_num == len(Lines):
			return accumulator
		if execution_tracker[line_num] == 1:
			# part 1
			# return accumulator
			# part 2
			return -1
		execution_tracker[line_num] += 1

		parts = Lines[line_num].split(" ")

		sign = 1

		if parts[1][0] == "-":
			sign = -1

		step = sign * int(parts[1][1:])

		if (parts[0] == "nop"):
			# part 2
			if switch_nop == line_num:
				line_num += step
			else:
				line_num += 1
		if (parts[0] == "acc"):
				accumulator += step
				line_num += 1
		if (parts[0] == "jmp"):
			# part 2
			if switch_jmp == line_num:
				line_num += 1
			else:
				line_num += step


def find_switch():
	for line in range(len(Lines)):
		if Lines[line][:3] == "jmp":
			result = execute(-1, line)
			if result > 0:
				return result
		if Lines[line][:3] == "nop" and Lines[line][5] != "0":
			result = execute(line, -1)

			if result > 0:
				return result
print(find_switch())