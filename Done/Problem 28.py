N = 1
compte = 1
n = 1
i = 1
while 2*N+1 <= 1001:
    for j in range(0, 4):
        n += 2*i
        compte += n
    N += 1
    i += 1

print(compte)