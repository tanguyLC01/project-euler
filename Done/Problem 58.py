import numpy as np

def premier(p):
    if p == 1:
        return False
    if all(p % i for i in range(2, int(p**0.5)+1)):
        return True
    return False

#def tour(spiral, a, b, n, i):
    # for j in range(2*i):
    #     spiral[b-j, a] = n
    #     n += 1
    # for j in range(1, 2*i+1):
    #     spiral[b-(2*i-1), a-j] = n
    #     n += 1 
    # for j in range(1, 2*i+1):
    #     spiral[b-(2*i-1)+j, a-(2*i-1)-1] = n
    #     n += 1
    # for j in range(2*i):
    #     spiral[b+1, a-(2*i-1)+j] = n
    #     n += 1
    # return n

# def creer_spiral(N):
#     spiral = np.zeros((2*N+1, 2*N+1), int)
#     n = 1
#     a = N
#     b = N
#     spiral[a, b] = n
#     n += 1
#     a += 1
#     for i in range(1, N+1):
#         n = tour(spiral, a, b, n, i)
#         a += 1
#         b += 1
#     return spiral

# def recup_diagonal(spiral):
#     n = len(spiral)
#     res = [[], []]
#     for i in range(n):
#         res[0].append(spiral[i, i])
#         if i != N:
#             res[1].append(spiral[i, n-1-i])
#     return res

def count_premier(l):
    l = list(map(premier, l))
    return sum(l)

N = 0
n = 1
j = 1
compte = 0
prop = compte/(4*N+1)
while prop > 0.1 or N == 0 and N < 4:
    N += 1
    bout = []
    for i in range(0, 4):
        n += 2*j
        bout.append(n)
    compte += count_premier(bout)
    prop = compte/(4*N+1)
    j += 1

print(N)