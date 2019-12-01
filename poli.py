str = input("Input to check if it is polydrum: ")
rstr = ''.join(reversed(str))
if str == rstr:
    print(str,"is polydrum")
else:
    print(str,"is not polydrum")

rstr = ','.join(reversed(str))
print(rstr)