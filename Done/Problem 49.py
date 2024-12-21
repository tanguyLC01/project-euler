import os

def premier(p):
    if all(p % i for i in range(2, int(p**0.5)+1)):
        return True
    return False

def permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


N = 3330
n = 1488
while True:
    if premier(n) and premier(n+N) and premier(n+2*N):
        if permutation(n, n+N) and permutation(n, n+2*N):
            break
    n += 1

print(int(str(n) + str(n+N) + str(n+2*N)))
os.system("Pause")