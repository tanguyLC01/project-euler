import string
possible_password = []
charac = []
with open("C:/Users/tlc29/Code/Project Euler/p059_cipher.txt", 'r') as file:
    charac = file.readlines()[0].split(',')
    i = 0
    k = 0
    while i < len(charac)-2:
        possible_password.append([])
        for j in range(i, i+3):
            possible_password[k].append(charac[j])
        i += 3
        k += 1


def decode(chaine, password):
    i = 0
    res = ""
    while i < len(chaine):
        if (i+2) < len(chaine):
            for j in range(i, i+3):
                res += (chr(int(password[j-i])^int(chaine[j])))
        i += 3
    return res


# text = []
# for i in range(15):
#     temp = decode(charac, possible_password[i])
#     text.append(temp)

print(decode(charac, possible_password[3]))