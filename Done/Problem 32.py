import os

def isPandigital(n):
    return "".join(sorted(str(n))) == "123456789"
compte = 0
previous = []
for i in range(1, 101):
    j = 100
    temp = i*j
    while temp < 10000:
        if isPandigital(str(i) + str(j) + str(temp)) and not temp in previous:
            compte += temp
            previous.append(temp)
        j += 1
        temp = i*j

print(compte)
print(previous)
os.system("Pause")