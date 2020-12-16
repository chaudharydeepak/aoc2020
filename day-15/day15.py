def part_1(input_seq):
	turn = 0

	age = {}

	while turn < 29999999:
		if input_seq[turn] not in age.keys():
			age[input_seq[turn]] = [turn, turn]
		else:
			age[input_seq[turn]] = [age[input_seq[turn]][1], turn]

		if turn == (len(input_seq) - 1):
			input_seq.append(age[input_seq[turn]][1] - age[input_seq[turn]][0])
		turn += 1
	return input_seq[-1]

print(part_1([0,1,5,10,3,12,19]))