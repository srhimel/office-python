def namota(number):
    for i in range(11):
        namota = i*number
        print(number, "x", i, "=", namota)
while True:
    number = input("kotor ghorer namota? ")
    number = int(number)
    namota(number)