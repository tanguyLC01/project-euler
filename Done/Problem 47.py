import os
def premier(p):
    if all(p % i for i in range(2, int(p**0.5))):
        return True
    return False

def ajout_dico(elem, dico):
    if elem in dico.keys():
        dico[elem] += 1
    else:
        dico[elem] = 1
    return dico

def to_num(dico):
    res = []
    for key in dico.keys():
        res.append(key*dico[key])
    return res

def prime_factors(n, divisors):
    p = 2
    while p**2 < n:
        if n % p == 0 and premier(p):
            divisors = ajout_dico(p, divisors)
            return prime_factors(n/p, divisors)
        p += 1
    divisors = ajout_dico(int(n), divisors)
    divisors = to_num(divisors)
    return divisors

def distinct(l):
    all_num = l[0] + l[1] + l[2] + l[3]
    for i in range(len(all_num)):
        for j in range(i+1, len(all_num)):
            if all_num[i] == all_num[j]:
                return False
    return True  

def find_four_p():
    n = 2
    while True:
        temp = prime_factors(n, {})
        four_p = []
        if len(temp) == 4:
            j = n+1
            four_p.append(temp)
            while j <= n+3:
                temp = prime_factors(j, {})
                if len(temp) != 4:
                    break
                four_p.append(temp)
                j += 1
            if len(four_p) == 4:
                if distinct(four_p):
                    return four_p
        n += 1

print(find_four_p())

#a = prime_factors(170, {}) + prime_factors(171, {})
#print(a)
os.system("Pause")