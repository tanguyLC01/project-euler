from fractions import Fraction

def calc_seq(b):
    if len(b) == 1:
        return b[0]
    temp = Fraction(1, b[len(b)-1])
    for i in range(len(b)-2, -1, -1):
        temp = 1/(b[i] + temp)
    return temp

# def calc_rec(b, n):
#     if n == 0:
#         return 0
#     return 1/(calc_rec(b, n-1)+calc_seq(b))

N = 99
seq = []
i = 1
while len(seq) < 3*(N//3):
    seq += [1, 2*i, 1]
    i += 1
while len(seq) < N:
    seq += [1]


num = str((2+calc_seq(seq)).numerator)
res = sum([int(i) for i in num])
print(res)