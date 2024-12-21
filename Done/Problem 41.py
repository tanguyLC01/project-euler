import os
from itertools import permutations

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
    return True

m = 0
for n in range(2, 10):
    pan = list(permutations([i for i in range(1, n)]))
    res = []
    for i in range(len(pan)):
        res.append([])
        for j in range(len(pan[i])):
            res[i].append(str(pan[i][j]))

    res = list(map("".join, res))
    res = list(map(int, res))

    maximum = 0
    for n in res:
        if isPrime(n) and maximum < n:
            maximum = n
    if maximum > m:
        m = maximum

print(m)

os.system("Pause")