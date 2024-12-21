# Equation :
# z = (1 + sqrt(4n^2 + 4n + 1))/ 4
# p = (1 + sqrt(12n^2 + 12n + 1))/6

def isPentagonal(n):
    # cf second equation
    return (1 + (12 * n ** 2 + 12 * n + 1 )**0.5)/6 == int((1 + (12 * n ** 2 + 12 * n + 1 )**0.5)/6)

def isHexagonal(n):
    # cf first equation
    return (1 + (4 * n ** 2 + 4 * n + 1)**0.5)/4 == int((1 + (4 * n ** 2 + 4 * n + 1)**0.5)/4)

t = 286
found = True
while found:
    if isPentagonal(t) and isHexagonal(t):
        found = False
    print(t)
    t += 1


