file1 = open('input.txt', 'r') 
Lines = file1.readlines() 


# Part 1

# mapping of color: colors which can contain key color
parents = {}

for line in Lines:
	contents = line.split("contain")
	parent = contents[0].split(" ")
	parent = parent[0] + " " + parent[1]

	children = contents[1][1:].split(", ")
	for child in children:
		bag = child.split(" ")
		if bag[0] == "no":
			continue
		bag = bag[1] + " " + bag[2]

		if bag not in parents:
			parents[bag] = {parent}
		else:
			parents[bag].add(parent)
		# print(bags[1] + " " + bags[2])
		# print(bag, parents[bag])
	# print(children)


def traverse_parents(bag, parents, gold_set):
	if bag not in parents:
		gold_set.add(bag)
		return
	else:
		for parent in parents[bag]:
			gold_set.add(parent)
			traverse_parents(parent, parents, gold_set)

gold_set = set()

traverse_parents("shiny gold", parents, gold_set)

# remove dummy empty string
print("Part 1:", len(gold_set))


# Part 2

# mapping of color: colors contained by key color
childs = {}
# input translated into mapping of color : [amount, color], ...
encoded_lines = {}

for line in Lines:
	contents = line.split("contain")
	parent = contents[0].split(" ")
	parent = parent[0] + " " + parent[1]

	childs[parent] = set()
	encoded_lines[parent] = []

	children = contents[1][1:].split(", ")
	for child in children:
		bag = child.split(" ")
		if bag[0] == "no":
			continue
		bag_string = bag[1] + " " + bag[2]
		childs[parent].add(bag_string)
		encoded_lines[parent].append([int(bag[0]), bag_string])

# print(encoded_lines)


def traverse_childs(bag, encoded_lines, childs, total):
	if len(encoded_lines[bag]) == 0:
		return 0
	else:
		temp_total = 0
		for child in encoded_lines[bag]:
			temp_total += child[0] + child[0] * traverse_childs(child[1], encoded_lines, childs, total)
		return temp_total


print("Part 2:", traverse_childs("shiny gold", encoded_lines, childs, 0))








