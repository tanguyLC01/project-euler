""" Problem 6 of Project Euler """
import os
sum_square = sum(pow(ent, 2) for ent in range(101)) 
square_sum = pow(sum(ent for ent in range(101)), 2) 
print(square_sum - sum_square)
os.system("Pause")