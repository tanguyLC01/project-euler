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
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

dizaine = {
    0: '',
    1: 'teen',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

def decomp(n):
    hundred = 0
    ten = 0
    res = ''
    if n >= 100: # Then, there is hundred
        hundred = n // 100
        n -= hundred*100 # We reduce n by the hundred to get only ten and units
        if n == 0: #perfect hundred
            res += num_to_letters[hundred] + 'hundred'
        else:
            res += num_to_letters[hundred] + 'hundred' + 'and'
        
    unit = n
    if n >= 10:
        ten = n // 10
        unit = n % 10
        if ten == 1:    
            res += num_to_letters[unit + ten*10]
        else:
            res += dizaine[ten] + num_to_letters[unit]
    else:
        res += num_to_letters[unit]
    return res

print(decomp(888))
count = 0
for n in range(1, 1000):
    count += len(decomp(n))
      
    
print(count + 11) # We add 'onethousand'
os.system("Pause")