import os
fractions = []

def PGCD(a, b): #a/b
    while b != 0:
        q = int(a/b)
        r = a - b*q
        a = b
        b = r
    return a
 
m = 0
for d in range(2, 10**6):
    for temp in range(1, d):
        p = PGCD(d, temp)
        if p == 1:
            fractions.append(temp/d) 
        m = len(fractions)//2

print(len(fractions))
os.system("Pause")