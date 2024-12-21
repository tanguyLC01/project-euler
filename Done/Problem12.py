""" Problem 12 of Project Euler """
"""Not Finished """


def triangle(n):
	return (n * (n +1)) / 2

def isPrime(n):
	return all(n % i for i in range(2, int(n**0.5) + 1))

def nDivisors(n):
	i = 2 # 1 and n are divisors of n
	for d in range(2, int(n**0.5) + 1):
		if n % d == 0:
			i += 2
	return i
divisors = 0

i = 1
while divisors <= 500:
	n = triangle(i)
	divisors = nDivisors(n)
	i += 1
	
print(n)