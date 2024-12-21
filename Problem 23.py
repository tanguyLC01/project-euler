import os

def isAbundant(n):
    res = 1
    for ent in range(2, int((n/2)**0.5)):
        if n % ent == 0:
            res += ent
            if n/ent != ent:
                res += n/ent
        if res > n:
            return True
    return res > n

print(isAbundant(6))
n= 28123
abundants = [i for i in range(2, n) if isAbundant(i)]
print(len(abundants))
somme = n*(n+1)/2
print(somme)
for i in range(1, n):
    for j in abundants:
        if i-j <= 0:
            break
        if isAbundant(i-j):
            somme -= i
print(somme)
os.system("Pause")