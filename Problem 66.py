import os


x = 0
largestD = 0
for d in range(2, 1000):
    if d**0.5 != int(d**0.5):
        i = 1
        while True:
            temp = 1 + d * i ** 2
            if temp**0.5 == int(temp**0.5): 
                if temp > x:
                    largestD = d
                    x = temp
                break
            i += 1
            
    if not d % 10:
        print("{} %".format(d/1000 * 100))
print(largestD, x)

os.system("Pause")