import os
def isPrime(n):
    return all(n % i for i in range(2, int(n**0.5) + 1))

def sieves(n): # Implementation of erastothene alogrithm
    primes = [True] * n
    primes[0] = primes[1] = False

    for (i, prime) in enumerate(primes):
        if prime:
            yield i
            for j in range(i**2, n, i):
                primes[j] = False

def circle(n):
    return int(str(n)[1:] + str(n)[0])

def multiple_of_two(n):
    for i in range(0, 10, 2):
        if str(i) in str(n):
            return False
    return True

count = 0
primes = list(sieves(10**6))
primes = list(filter(multiple_of_two, primes))

for n in primes:
    circular = True
    for i in range(len(str(n)) - 1):
        n = circle(n)
        if not n in primes:
            circular = False
            break
    if circular:
        count += 1

print(count+1) # We add one for number 2 
os.system("Pause")
