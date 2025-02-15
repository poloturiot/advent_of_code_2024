import numpy as np

def square_is_letter(row,column,x,y,letter):
    return 0 < row+y < len(matrix[row]) and 0 < column+x < len(matrix) and matrix[row+y,column+x] == letter

txt = open("input.txt").read().split("\n")

rows = [list(line) for line in txt]
matrix = np.array(rows)

adjacent = [[0,1],   # To the right
            [1,1],   # Down and to the right (diagonal)
            [1,0],   # Under
            [1,-1],  # Down and to the left (diagonal)
            [0,-1],  # To the left
            [-1,-1], # Up and to the left (diagonal)
            [-1,0],  # Above
            [-1,1]]  # # Up and to the right (diagonal)

xmas_counter = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row,column] == 'X':
            # print("X on " + str(row),str(column))
            # Find adjacent M
            for adjacent_letter in adjacent:
                y = adjacent_letter[0]
                x = adjacent_letter[1]
                if 0 < row+y < len(matrix[row]) and 0 < column+x < len(matrix) and matrix[row+y,column+x] == 'M':
                    # print("   M on " + str(row+y),str(column+x))
                    # keep same x and y and search for the other letters
                    if 0 < row+2*y < len(matrix[row]) and 0 < column+2*x < len(matrix) and matrix[row+2*y,column+2*x] == 'A':
                        # print("   A on " + str(row+2*y),str(column+2*x))
                        if 0 < row+3*y < len(matrix[row]) and 0 < column+3*x < len(matrix) and matrix[row+3*y,column+3*x] == 'S':
                            print("X on " + str(row),str(column))
                            print("M on " + str(row+y),str(column+x))
                            print("A on " + str(row+2*y),str(column+2*x))
                            print("S on " + str(row+3*y),str(column+3*x))
                            print("==========")
                            xmas_counter += 1

print(str(xmas_counter) + " XMAS in total")

