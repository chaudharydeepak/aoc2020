file1 = open('input.txt', 'r') 
Lines = file1.readlines() 



jolts = [int(i) for i in Lines]
# part 1
jolts.append(0)
# jolts.append(max(jolts)+3)
# jolts.sort()


# diffs = {0:0, 1:0, 2:0, 3:0}

# for i in range(0, len(jolts) - 1):
# 	diffs[jolts[i + 1] - jolts[i]] += 1

# print(diffs[1] * diffs[3])

# part 2

def connect_adapters(start, jolts_array, index, end, memos):


	if index >= len(jolts_array):
		return 0 

	if jolts_array[index] > start + 3:
		return 0
	if jolts_array[index] + 3 == end:
		return 1
	if memos[index] == -1:
		first = connect_adapters(jolts_array[index], jolts_array, index + 1, end, memos)
		second = connect_adapters(jolts_array[index], jolts_array, index + 2, end, memos)
		third = connect_adapters(jolts_array[index], jolts_array, index + 3, end, memos)
		memos[index] = first + second + third

	return memos[index]



memos = [-1] * len(jolts)

jolts.sort()
print(connect_adapters(0, jolts, 0, max(jolts) + 3, memos))