def isPrime(n):
    if all(n % i for i in range(2, int(n**0.5) + 1)):
        return True
    return False

def isComposite(n):
    return n % 2 and not isPrime(n)

def isTwiceSquare(n):
    n /= 2
    return n**0.5 == int(n**0.5)

print(isTwiceSquare(2))
n = 2
found  = True
while found:
    if isComposite(n):
        for p in range(2, n): # Look through every primes between [2;n]
            if isPrime(p) and isTwiceSquare(n - p):
                    break
            if p == n-1:
                found = False
    n += 1
    print(n)
print(n)
