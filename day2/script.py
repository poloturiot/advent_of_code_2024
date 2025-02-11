# file to data

# data = [*map(int, open("input.txt").read().split())]

# print(data)

# A = data[0:5]
# B = data[5:10]

# list_of_list = map(data)

# print(A)
# print(B)

def report_is_safe(data):
    result_list=[]
    for i in range(len(data)-1):
        result_list.append(data[i]-data[i+1])
    
    is_increasing = all(num in range (-3,0) for num in result_list)
    is_decreasing = all(num in range (1,4) for num in result_list)

    return is_increasing or is_decreasing

data = [[1, 2, 4, 5, 7], [1, 2, 4, 5, 1]]

result=list(map(report_is_safe, data))

print(result.count(True))
