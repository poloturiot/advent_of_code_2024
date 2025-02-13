import re

txt = open("input.txt").read()

matches = re.findall("(?<=mul\()(\d{1,3}),(\d{1,3})(?=\))", txt)

result = [int(match[0])*int(match[1]) for match in matches]

print(sum(result))