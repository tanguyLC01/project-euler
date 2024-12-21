solution = [0, 0] # [value, p]
for p in range(1, 1000):
    i = 0
    for c in range(1, int(p / 4) + 1):
        b = (p**2 - 2 * p * c) / (2 * (p - c))
        a = p - b - c
        if a**2 == b**2 + c**2 and a**2 == int(a**2):
            # It is a right angle triangle with integer length sides
            i += 1
    if i > solution[0]:
        solution[0] = i
        solution[1] = p
        
print(solution)