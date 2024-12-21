import os

def isPrime(n):
    n = int(n)
    if n == 1:
        return False
    if all(n%i for i in range(2, int(n**0.5)+1)):
        return True
    return False

t_primes = []
n = 10
while len(t_primes) < 11:
    if isPrime(n):
        truncable = True
        l = len(str(n))
        for i in range(1, l):
            if not isPrime(str(n)[:i]) or not isPrime(str(n)[i:]):
                truncable = False
                break
        if truncable:
            t_primes.append(n)
    n += 1
	

print(sum(t_primes))
print(t_primes)

os.system("Pause")