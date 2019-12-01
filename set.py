country1 = set("bangladesh")
country2 = set("sri lanka")

union = country1 | country2
print(union)
intersection = country1 & country2
print(intersection)
unique = country1 ^ country2
print(unique)
substract = country2 - country1
print(substract)

list = [1,2,3,4,5]
tuple = (6,7,8,9,10)

set1 = set(list)
set2 = set(tuple)
print(set1 , set2)

