""" Problem 9 of Project Euler """
import os
from math import *
c = 0
while c < 1000:
	b = 0
	while b < c:
		a = 0
		while a < b:
			if a + b + c == 1000 and a**2 + b**2 == c**2:
				print(a,b,c)
				break
			a += 1
		b += 1
	c += 1


os.system("Pause")