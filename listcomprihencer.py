li = [1,9,8,5]
newli = []
for i in li:
    newli.append(i*2)
print(newli)
newli = [2 * i for i in li]
print(newli)
li = [1,2,4,5,6,8,9,12,15,18]
newli2 =[]
for j in li:
    if j%2 == 0:
        newli2.append(j)
print(newli2)
newli2= [ j for j in li if j%2 == 0]
print(newli2)

li = [1,2,3,4]
newli3 = [x*x for x in li]
print(newli3)