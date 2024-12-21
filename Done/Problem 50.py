import os

def isPrime(n):
    if all(n % i for i in range(2, int(n**0.5) + 1)):
        return True
    return False


maxSolution = {
    "num": 0,
    "lengthPrimes": 0,
    "sumPrimes": 0,
}

for n in range(10**5, 10**6):
    if isPrime(n):
        primesAdded = []
        stop = False
        p = 2
        while not stop:
            if isPrime(p):
                while sum(primesAdded) > n:
                    primesAdded.pop(0)
                    stop = True
                    
                if sum(primesAdded) == n: 
                    stop = True
                   
                if not stop:
                    primesAdded.append(p)

            p += 1
           
        if sum(primesAdded) == n and len(primesAdded) > maxSolution["lengthPrimes"]:
            maxSolution["num"] = n
            maxSolution["lengthPrimes"] = len(primesAdded)
        
    if not n % 10000:
        print("{} %".format((n/ 10**6) * 100))
        
print(maxSolution["num"], maxSolution["lengthPrimes"])
os.system("Pause")
