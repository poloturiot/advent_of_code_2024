def get_distance_between_lists(list1, list2):
    total_distance = 0

    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])

        total_distance += distance

    return total_distance

def file_to_sorted_int_lists(file_name):
	list1 = []
	list2 = []

	f = open(file_name, "r")
	for x in f:
		stripped_split_line = x.strip().split()

		id1 = int(stripped_split_line[0])
		id2 = int(stripped_split_line[1])

		list1.append(id1)
		list2.append(id2)

	list1.sort()
	list2.sort()
      
	return [list1, list2]

# MAIN

[list1, list2] = file_to_sorted_int_lists("input.txt")

distance = get_distance_between_lists(list1, list2)

print(distance)
