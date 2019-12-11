n = int(input(" "))
if n%2 != 0:
    print("Weird")
if n%2 == 0:
    if n in range(2,5):
        print("Not Weired")
    elif n in range(6,20):
        print("Weired")
    elif n > 20:
        print("Not Weired")
