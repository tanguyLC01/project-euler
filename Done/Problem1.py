""" Problem1 of Project Euler"""
import os
i = 0
sum_mutiple = 0
while i < 1000:
	if i % 3 == 0:
		sum_mutiple += i
		done = True
	if i % 5 == 0 and done is not True:
		sum_mutiple += i 
	i += 1
	done = False

print(sum_mutiple)
os.system("Pause")