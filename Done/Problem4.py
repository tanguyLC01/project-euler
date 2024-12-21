"""Problem 4 of Project Euler"""
""" NOT WORKING """
import os
num = 0
i = 999
while i > 100:
	j = 999
	while j > 100:
		p = j * i
		first_list = [ent for ent in str(p)]
		k = len(first_list) - 1
		second_list = []
		while k > -1:
			second_list.append(first_list[k])
			k -= 1
		if first_list == second_list and p > num:
			num = p
			i = 0
			j = 0
		j -= 1
	i -= 1
print(num)
os.system("Pause")