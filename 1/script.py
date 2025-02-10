def string_to_sorted_list(list):
    new_list=[]
    for i in list:
        new_list.append(int(i))

    new_list.sort()

    return new_list

def get_distance_between_lists(list1, list2):
    total_distance = 0

    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])

        total_distance += distance

    return total_distance

# MAIN

# read file

total_distance = 0

f = open("input.txt", "r")
for x in f:
  stripped_split_line = x.strip().split()

  list1 = stripped_split_line[0]
  list2 = stripped_split_line[1]

  int_list1 = string_to_sorted_list(list1)
  int_list2 = string_to_sorted_list(list2)

  distance = get_distance_between_lists(int_list1, int_list2)

  total_distance += distance

print(total_distance)

