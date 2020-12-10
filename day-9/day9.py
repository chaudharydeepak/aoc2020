file1 = open('input.txt', 'r') 
Lines = file1.readlines() 


def check_prev_25(index):
	start = index - 25
	for x in range(start, index):
		for y in range(x + 1, index):
			# print ("adding", Lines[x], Lines[y], "sum", Lines[x] + Lines[y])
			if int(Lines[x]) + int(Lines[y]) == int(Lines[index]):
				return True
	return False

def part_1():
	for i in range(25, len(Lines)):
		if not check_prev_25(i):
			return i

print(Lines[part_1()])

def part_2():
	weakness = part_1()
	for i in range(weakness):
		total = 0
		inner_i = i
		while True:
			total += int(Lines[inner_i])
			if total >= int(Lines[weakness]):
				break
			inner_i += 1
		if total == int(Lines[weakness]):
			sublist = [int(i) for i in Lines[i:inner_i]]
			return min(sublist) + max(sublist)

print(part_2())