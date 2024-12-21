def isTriangle(t):
    return (1 + (1 + 8 * t) ** 0.5)/2 == int((1 + (1 + 8 * t) ** 0.5)/2)

words = []
with open("Problem 42 Data.py", "r") as f:
    for ent in f:
        words.append(ent)

words = words[0].split(",")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0
for word in words:
    value = 0
    for letter in word:
        value += (alphabet.find(letter) + 1)
    if isTriangle(value):
        count += 1

print(count)