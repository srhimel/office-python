marks = [78,74,75,76,15,11,100]
roll = input("What is your roll number? :  ")
print("Your mark is :",marks[int(roll)-1])

multimarks = {"rahim": {"bangla": 50, "english": 45}, "karim": {"bangla": 50, "english": 45}}
name = input("Tor nam ki? ")
subject = input("tui kier mark janbar cas? bangla naki english?")
print("Tui", subject, "te paicos", multimarks[name][subject])


