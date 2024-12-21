

f_n = 0
f_n1 = 1
i = 2
res = 0
while i < 91:
    f_n2 = f_n + f_n1
    for n in range(f_n1+1, f_n2+1):
        res += int(str(n % 9)+'9'*(n//9))
    f_n = f_n1
    f_n1 = f_n2
    i += 1
    print(i)

print(res % 1000000007)
