import os

def premier(p):
    if all(p%i for i in range(2, int(p**0.5)+1)):
        return True
    return False

def div_premier(n, divisors = []):
    p = 2
    while p**2 <= n:
        if n % p == 0 and premier(p):
            if p not in divisors:
                divisors.append(p)
            return div_premier(n/p, divisors.copy())
        p += 1
    return divisors

def multiply(l):
    res = 1
    for i in l:
        res *= (1-1/i)
    return res

m = 2
q = 1
for n in range(2, 10**6+1):
    phi = n*multiply(div_premier(n))
    if n/phi > q:
        q = n/phi
        m = n
    if n % 10**5 == 0 and n > 10**5:
        print(n)

print(m)
    
os.system("Pause")