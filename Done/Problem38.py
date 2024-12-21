import os

def isPandigital(n):
    n = str(n)
    previousNums = []
    for elem in n:
        if elem in previousNums:
            return False
        previousNums.append(elem)
    return True
    
pan = 0
i = 0
for n in range(1, 10000):
    string = ""
    i = 1
    while len(string) < 9:
        string += str(n * i)
        i += 1
        
    if len(string) == 9 and isPandigital(int(string)) and pan < int(string):
        pan = int(string)
        print(n)

print(pan, i - 1)
os.system("Pause")