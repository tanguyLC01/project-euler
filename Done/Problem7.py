""" Problem 7 of Project Euler """
import os
from math import sqrt
def is_prime(n):
	i = 2
	while i <= sqrt(n):
		if n % i == 0:
			return False
		i += 1
	return True

i = 0
j = 0
while j != 6:
	i += 2
	if is_prime(i):
		j += 1
	


print(i)
print(j)
os.system("Pause")

