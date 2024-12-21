keylog = []
with open("./keylog.txt", 'r') as file:
    for ent in file.readlines():
        keylog.append(ent.strip())

previous = {}
for num in keylog:
    first, second, end = list(num)
    if end in previous:
        if not second in previous[end]:
            previous[end].append(second)
    else:
        previous[end] = []
    if second in previous:
        if not first in previous[second]:
            previous[second].append(first)
    else:
        previous[second] = []
    if not first in previous:
        previous[first] = []
print(previous)
73162890
