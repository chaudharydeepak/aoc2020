file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
p1_count = 0
p2_count = 0

for line in Lines: 
	# split at the colon
    colon_split = line.split(":")
    
    # get the password parameters and the password itself
    params = colon_split[0]
    password = colon_split[1]

    # extract the indices and the specific letter 
    num_letter = params.split(" ")
    nums = num_letter[0].split("-")
    letter = num_letter[1][0]

    # part 1 tally
    occurrences = password.count(letter)
    if (occurrences >= int(nums[0]) and occurrences <= int(nums[1])):
    	p1_count+=1

    # part 2 tally
    if (password[int(nums[0])] == letter):
    	if (password[int(nums[1])] != letter):
    		p2_count += 1
    elif (password[int(nums[1])] == letter):
    		p2_count += 1

print("Part 1:")
print(p1_count)
print("Part 2:")
print(p2_count)