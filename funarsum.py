def find(countries,country):
    if country in countries:
        print(country, "Found in the array")
    else:
        print(country, "Not found")
countries = ["Bangladesh","Vutan"]
find(countries,"Bangladesh")
while True:
    names = ["Ratul", "prodip", "cerag"]
    name = input("Kare khujo ?: ")
    find(names,name)