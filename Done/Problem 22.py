def restruct(string):
    return "".join([string[i] for i in range(1, len(string) - 1)])


names = []
with open("Problem 22 Data.py", "r") as f:
    for ent in f:
        names = list(map(restruct, ent.split(',')))

names.sort()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(names))
count = 0
for index, name in enumerate(names):
    value = 0
    for letter in name:
        value += (alphabet.find(letter) + 1)
    value *= (index+1)
    if name == "COLIN":
        print(value, index)
    count += value

print(count)
