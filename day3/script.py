import re

txt = open("input.txt").read()

matches = re.findall("(?<=mul\()(\d{1,3}),(\d{1,3})(?=\))|(do\(\))|(don't\(\))", txt)

enabled = True

results=0

for a, b, do, dont in matches:
    if do or dont:
        enabled = bool(do)
    else:
        result = int(a) * int(b) * enabled
        results += result

print(results)