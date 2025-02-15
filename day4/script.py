import numpy as np

txt = open("input.txt").read().split("\n")

rows = [list(line) for line in txt]
matrix = np.array(rows)
print(matrix[2,4])

# for row in rows:
#     for letter in row:
#         if letter == 'X':
#             # look for M in adjacent letters
