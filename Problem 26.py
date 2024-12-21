import re
pattern = re.compile(r"([0-9]+?)\1+")

maximum = [0, 0]

for d in range(1, 1000):
    temp = pattern.findall(str(1/d)[2:])
    if temp != [] and (len(temp) == 1 or (len(temp) == 2 and temp[0] == '0')):
        if len(temp[0]) >= maximum[0]:
            maximum[0] = len(temp[0])
            maximum[1] = d


print(pattern.findall(str((1/730))[2:]))
print(maximum)