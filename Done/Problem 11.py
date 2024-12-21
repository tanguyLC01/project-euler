import os
values = []

with open("Problem 11 Data.txt", "r") as f:
    for line in f:
        if line[0] == '\n':
            continue
        line = line[:(len(line) - 1)]
        values.append(list(map(int, line.split(" "))))
       
highest_product = 0   

# For each number, we have to check whether we can go left, right, down, up or/and diagonally.

        
for i in range(3, len(values) - 3):
    for j in range(3, len(values[i]) - 3):
        line = values[i]
        #Right
        product = line[j] * line[j + 1] * line[j + 2] * line[j + 3]
        
        #Left
        product = max(product, line[j] * line[j-1] * line[j-2] * line[j-3])
        
        #Up
        product = max(product, values[i][j] * values[i-1][j] * values[i-2][j] * values[i-3][j])
            
        #Down
        product = max(product, values[i][j] * values[i+1][j] * values[i+2][j] * values[i+3][j])
        
        #Diagonally Left Up
        product = max(product, values[i][j] * values[i-1][j-1] * values[i-2][j-2]* values[i-3][j-3])
        
        #Diagonally Left Down
        product = max(product, values[i][j] * values[i+1][j-1] * values[i+2][j-2]* values[i+3][j-3])
        
        #Diagonally Right Up
        product = max(product, values[i][j] * values[i-1][j+1] * values[i-2][j+2] * values[i-3][j+3])
        
        #Diagonally Right Down
        product = max(product, values[i][j] * values[i+1][j+1] * values[i+2][j+2] * values[i+3][j+3])
        
        highest_product = max(product, highest_product)
        
print(highest_product)
os.system("Pause")