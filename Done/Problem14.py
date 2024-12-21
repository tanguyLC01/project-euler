""" Project 14 of Project Euler """
import os

def collatz(n):
	if n % 2 == 0:
		return n/2
	return 3*n+1

temp = 0
count = 0
for i in range(2, 999999):
	j = 0
	n = i
	while n != 1:
		n = collatz(n)
		j += 1
	if j > count:
		count = j
		temp = i

os.system("Pause")
