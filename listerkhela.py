bazar = ["alu", "potol", "piaz"]
bazar.append("Doi")
bazar.insert(0,"Kumra")
kinumna = "piaz"
if kinumna in bazar:
    bazar.remove("piaz")
    print("Piaz khao bondho")
bazar.sort()
for list in bazar:
    print("Kinum",list)
item = bazar.pop(1)
print(item)
print(bazar)

num = [8,56,4,1,9]
num.sort()
print(num)

num1 = [10,12,15,17,18,3]
num2 = [6,12,14,18,20]

num1.extend(num2)
print(num1)
print(num1.count(12))

del(num1[5])
print(num1)

li = []
for i in range(2,50,3):
    li.append(i)
print(li)

li2 = li +li

print(li2)

li2 = li2 * 3
print(li2)

bazar = "-".join(bazar)
print(bazar)