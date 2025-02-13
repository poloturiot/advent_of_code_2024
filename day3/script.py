import re

txt = open("input.txt").read()

matches = re.findall("(?<=mul\()[0-9]{1,3}(?=,[0-9]{1,3}\))|(?<=mul\([0-9]{1,3},)[0-9]{1,3}(?=\))", txt)

print(matches)