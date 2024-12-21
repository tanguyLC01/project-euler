import numpy as np
maximum = 0
i = 1
with open("C:\\Users\\tlc29\\Code\\Project Euler\\p099_base_exp.txt", "r") as file:
    for (j, ligne) in enumerate(file.readlines()):
        base, exposant = ligne.split(",")
        base = int(base)
        exposant = int(exposant)
        if exposant*np.log(base) > maximum:
            i = j
            maximum = exposant*np.log(base)

print(i+1)