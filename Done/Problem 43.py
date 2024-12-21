import os

def conversion(n):
    n = str(n)
    if len(n) == 2:
        return "0"+n
    return n

m_two = map(conversion, [i for i in range(10, 1000) if i % 2 == 0 and len(set(str(i))) == 3])

def all_different(elem):
    # function to check if all the elements of "elem" are different
    return all(elem.count(ent) == 1 for ent in elem)

def is_pandigital(n):
    return "".join(sorted(str(n))) == "0123456789"

# print(same_digits("063", "406"))
# print(process("406", map(conversion, [63, 104, 502])))

def add_and_div(number, d):
    n = number[len(number) - 2] + number[len(number) - 1]
    for i in range(0, 10):
        temp = int(n + str(i))
        if temp % d == 0:
            yield conversion(temp)

def process(elements, d):
    # We filter the elements that have all different digit 
    return list(filter(all_different, list(add_and_div(elements, d))))

def last(n):
    return n[len(n) - 1]

count = 0
for two in m_two:
    two = str(two)
    list_three = process(two, 3)
    for three in list_three:
        three = str(three)
        list_five = process(three, 5)
        for five in list_five:
            five = str(five)
            list_seven = process(five, 7)
            for seven in list_seven:
                seven = str(seven)
                list_eleven = process(seven, 11)
                for eleven in list_eleven:
                    eleven = str(eleven)
                    list_thirteen = process(eleven, 13)
                    for thirteen in list_thirteen:
                        thirteen = str(thirteen)
                        list_seventeen = process(thirteen, 17)
                        for seventeen in list_seventeen:
                            n = two + last(three) +last(five) + last(seven) + last(eleven) + last(thirteen) + last(seventeen)
                            first_digit = [str(i) for i in range(1,10) if not str(i) in n][0]
                            n = first_digit + n
                            if is_pandigital(n):
                                count += int(n)

print(n)
print(count)


os.system("Pause")
