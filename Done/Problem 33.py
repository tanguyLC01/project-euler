def isSimplyfiable(a, b):  # a < b
    fraction = a/b
    if "0" in str(a) or "0" in str(b):
        return
    for i, num in enumerate(str(a)):
        for j, den in enumerate(str(b)):
            if num == den and num != 0:  # Could be "den" because we check equality before
                if fraction == int(str(a)[1-i])/int(str(b)[1-j]):
                    return (a, b)


values = []
i = 0
for num in range(11, 99):
    for den in range(11, 99):
        if den != num:
            value = isSimplyfiable(num , den)
            if (value):
                values.append(value)

print(values)
