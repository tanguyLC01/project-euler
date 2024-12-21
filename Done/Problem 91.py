import os
import numpy as np

n = 50
points = [(x, y) for x in range(0, n+1) for y in range(0, n+1)]
points.remove((0, 0))
count = 0
for x1, y1 in points:
    for x2, y2 in points:
        if (x1, y1) == (x2, y2):
            continue
        if x1*(x2 - x1) + y1*(y2 - y1) == 0: # (x2, y2) is normal
            count += 1

print(count + n**2) # From the origin, we have n**2 normal vectors possible.

os.system("PAUSE")