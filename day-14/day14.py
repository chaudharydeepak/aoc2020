def eval_val1(value):
	total = 0
	for i in range(len(value)):
		total += 2 ** (35-i) * int(value[i])
	return total

def eval_val2(value, val_index, mem_val, mem):
	if val_index == (len(value) - 1) and value[val_index] != "X":
		mem[eval_val1("".join(value))] = mem_val

	if value[val_index] == "X":
		value[val_index] = "0"
		eval_val2(value, val_index, mem_val, mem)
		value[val_index] = "1"
		eval_val2(value, val_index, mem_val, mem)
		value[val_index] = "X"
	elif val_index < len(value) - 1:
		eval_val2(value, val_index + 1, mem_val, mem)

def parse_val(line):
	parts = line.split(" = ")
	index = int(parts[0][4:-1])
	value = int(parts[1])
	return index, value

def parse_mask(line):
	parts = line.split(" = ")
	return parts[1]

def convert_to_binary(number):
	return format(number, '036b')

def apply_mask1(number, mask):
	new_string = list(number)
	for i in range(len(mask)):
		if mask[i] == "1":
			new_string[i] = "1"
		elif mask[i] == "0":
			new_string[i] = "0"
	return "".join(new_string)

def apply_mask2(number, mask):
	new_string = list(number)
	for i in range(len(mask)):
		if mask[i] == "1":
			new_string[i] = "1"
		elif mask[i] == "X":
			new_string[i] = "X"
	return "".join(new_string)

def part_1():
	file1 = open('input.txt', 'r') 
	Lines = file1.readlines() 

	mem = {}

	mask = ""

	for line in Lines:
		if line[:4] == "mask":
			mask = parse_mask(line)
			continue
		index, value = parse_val(line)
		binary_val = convert_to_binary(value)
		mem[index] = eval_val1(apply_mask1(binary_val, mask))
	
	total = 0
	for key in mem:
		total += mem[key]
	return total

def part_2():
	file1 = open('input.txt', 'r') 
	Lines = file1.readlines() 

	mem = {}

	mask = ""

	for line in Lines:
		if line[:4] == "mask":
			mask = parse_mask(line)
			continue
		index, value = parse_val(line)
		# PART 1
		# binary_val = convert_to_binary(value)
		# mem[index] = eval_val1(apply_mask1(binary_val, mask))
		# PART 2
		binary_index = convert_to_binary(index)
		eval_val2(list(apply_mask2(binary_index, mask)), 0, value, mem)
	
	total = 0
	for key in mem:
		total += mem[key]
	return total



print(part_1())
print(part_2())

# print(eval_val("000000000000000000000000000000001011"))

# print(parse_val("mem[18848] = 944747776"))

# print(parse_mask("mask = 01101111X0110X00XX00000110X00101X001"))