def report_is_safe(report):
    
    result_list=[report[i]-report[i+1] for i in range(len(report)-1)]

    return set(result_list) <= {1,2,3} or set(result_list) <= {-1, -2, -3}

data = [[int(x) for x in y.split(" ")] for y in open("input.txt").read().split("\n")]

print(sum([report_is_safe(report) for report in data]))

safe_count = sum([any([report_is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)