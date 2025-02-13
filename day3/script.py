import re

txt = open("input.txt").read()

matches = re.findall("(?<=mul\()\d{1,3},\d{1,3}(?=\))|do\(\)|don't\(\)", txt)

# print(matches)

enabled = True

results=[]

for match in matches:
    # print(enabled)
    if match == "don't()":
        enabled = False
    elif match == "do()":
        enabled = True
    elif enabled:
        args = [int(i) for i in match.split(",")]
        result = args[0] * args[1]
        results.append(result)
        # print(match + "=" + str(result))
    # else :
        # print(match, "Not enabled")

print(sum(results))

# result = [int(match[0])*int(match[1]) for match in matches]

# print(sum(result))