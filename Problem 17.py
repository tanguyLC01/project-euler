import os

num_to_letters = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'heigth',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
}

dizaine = {
    0: '',
    1: 'teen',
    2: 'twen',
    3: 'thir',
    4: 'for',
    5: 'fif',
    6: 'six',
    7: 'seven',
    8: 'height',
    9: 'nine',
}

def decomp(n):
    hundred = 0
    ten = 0
    if n >= 100: # Then, there is hundred
        hundred = int(str(n)[0])
        n -= hundred*100 # We reduce n by the hundred to get only ten and units
    if n >= 10:
        ten = int(str(n)[0])
        n -= ten*10
    unit = int(str(n)[0])
    if hundred:
        s = ""
        if ten:
            s = dizaine[ten] + 'ty'
        return s + num_to_letters[unit] + 'and' + num_to_letters[hundred] + 'hundred' # 3 corresponds to 'and'
    return num_to_letters[unit] + dizaine[ten] + 'ty'

count = 0
for n in range(1, 1000):
    if n < 16:
        count += len(num_to_letters[n])
    else:
        count += len(decomp(n))
      
    
print(count + 11) # We add 'one thousand'
os.system("Pause")