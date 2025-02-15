import numpy as np

def square_is_letter(row,column,x,y,letter):
    # print("Checking on [" + str(row+y) + "," + str(column+x) +"]")
    if not 0 <= row+y < len(matrix[row]) or not 0 <= column+x < len(matrix) :
        # print("[" + str(row+y) + "," + str(column+x) +"] out of bound")
        return False
    elif matrix[row+y,column+x] == letter:
        # print(letter + " on " + str(row+y),str(column+x))
        return True
    else:
        return False

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
        if square_is_letter(row,column,0,0,'X'):
            for adjacent_letter in adjacent:
                y = adjacent_letter[0]
                x = adjacent_letter[1]
                if square_is_letter(row,column,x,y,'M'):
                    if square_is_letter(row,column,2*x,2*y,'A'):
                        if square_is_letter(row,column,3*x,3*y,'S'):
                            print("X on " + str(row),str(column))
                            print("M on " + str(row+y),str(column+x))
                            print("A on " + str(row+2*y),str(column+2*x))
                            print("S on " + str(row+3*y),str(column+3*x))
                            print("==========")
                            xmas_counter += 1

print(str(xmas_counter) + " XMAS in total")