""" Problem 10 of Project Euler """

import os
print(sum(n for n in range(2, 2000001) if all(n % i for i in range(2, int(n**0.5) + 1))))

os.system("Pause")