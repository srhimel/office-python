def sebalada(str):
    a = ''
    b = ''
    c = ''
    d = ''
    for i in str:
        if i.isupper():
            a += i
        elif i.islower():
            b += i
        elif i.isdigit():
            c += i
        elif not i.isupper() and not i.islower() and not i.isdigit():
            d += i
    return a, b , c , d

arrray = sebalada("Hello Test! 123 123, good.")
for j in arrray:
    print(j)