def solution(a, b, c):
    delta = b**2-4*a*c
    if delta < 0:
        return None
    if delta == 0:
        return [-b/(2*a)]
    return [-b/(2*a) + (delta**0.5)/(2*a), -b/(2*a) - (delta**0.5)/(2*a)]

def solution_entiere(solution):
    if solution is None:
            return False
    solution = list(filter(lambda x: x>0, solution))
    solution_entier = list(map(entier, solution))
    return any(solution_entier)

def entier(n):
    return int(n) == n

def profondeur(l):
    if type(l) is int:
        return 1
    return 1+profondeur(l[0])

def cyclique(l, n, d):
    if l == []:
        return False
    p = profondeur(l)
    if p < d:
        return False
    return False


def triangle(n):
    temp = solution(1, 1, -2*n)
    return solution_entiere(temp)

def square(n):
    return int(n**0.5) == n**0.5

def pentagonal(n):
    temp = solution(3, -1, -2*n)
    return solution_entiere(temp)

def hexagonal(n):
    temp = solution(2, -1, -n)
    return solution_entiere(temp)

def heptagonal(n):
    temp = solution(5, -3, -2*n)
    return solution_entiere(temp)

def octogonal(n):
    temp = solution(3, -2, -n)
    return solution_entiere(temp)

def exist_num(last, f):
    res = []
    for i in range(10, 100):
        b = f(int(last + str(i)))
        if b:
            res.append(int(last + str(i)))
    return res
    
def find_a_possible(last, l):
    if len(l) == 1:
        return exist_num(last, l[0])
    c = [[] for i in range(len(l))]
    j = 0
    a = exist_num(last, l[j])
    while a == [] and j < len(l)-1:
        j += 1
        a = exist_num(last, l[j])
    if len(a) != 0:
        l.remove(l[j])
        for i in range(len(a)):
            last = str(a[i])[2:]
            temp = find_a_possible(last, l)
            if temp != []:
                for elem in temp:
                    c.append([a[i], elem])
    return c

def ordered_set():
    for n in range(10**3+1, 10**4):
        l = [triangle, square, pentagonal, hexagonal, heptagonal, octogonal]
        if l[0](n): 
            l.remove(l[0])
            last = str(n)[2:]
            temp = find_a_possible(last, l)
            temp = list(filter(lambda x: x, [cyclique(i, n, d) for i in temp]))
            print(temp)
            if temp != [] and l[0] is not int:
                return [n, temp[0]]
d = 5
                
# print(triangle(8128))
#temp = find_a_possible("28", [square, pentagonal])
#print(list(filter(lambda x: x, [cyclique(i, 8128, d) for i in temp])))
print(ordered_set())
                

