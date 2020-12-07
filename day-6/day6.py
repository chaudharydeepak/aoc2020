file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

# part 1
# total = 0

# group_answers = {}

# for line in Lines:
# 	for char in range(len(line)):
# 		group_answers[line[char]] = ""
# 	if (line[0] == '\n'):
# 		group_answers.pop('\n', None)
# 		total += len(group_answers.keys())
# 		group_answers = {}
# # account for last group because there is no trailing newline
# group_answers.pop('\n', None)
# total += len(group_answers.keys())

# print(total)
total = 0
group_size = 0
group_answers = {}

for line in Lines:

	for char in range(len(line)):
		if (line[char] in group_answers):
			group_answers[line[char]] += 1
		else:
			group_answers[line[char]] = 1
	group_size += 1

	if (line[0] == '\n'):
		group_answers.pop('\n', None)
		group_size -= 1
		for key in group_answers.keys():
			if group_answers[key] == group_size:
				total += 1
		group_size = 0
		group_answers = {}
		
# # account for last group because there is no trailing newline
group_answers.pop('\n', None)
for key in group_answers.keys():
	if group_answers[key] == group_size:
		total += 1

print(total)