def pentagonal(n):
    return n * (3 * n - 1) / 2


def isPentagonal(n):
    calcul = (1 + (24 * n + 1)**0.5)/6
    return calcul == int(calcul)


print(isPentagonal(5482660))
k = 1
found = True
while found:
    for j in range(1, k):
        kPentagonal = pentagonal(k)
        jPentagonal = pentagonal(j)
        if isPentagonal(kPentagonal + jPentagonal) and isPentagonal(kPentagonal - jPentagonal):
            found = False
            break
    print(k)
    k += 1
print(kPentagonal, jPentagonal)
