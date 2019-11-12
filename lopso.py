terminate = False
allowed = ["sum", "sub", "multiply", "devide", "modulas", "reset", "exit"]
while not terminate:
    n1 = input("Give the number 1: ")
    n1 = int(n1)
    n2 = input("Give the number 2: ")
    n2 = int(n2)
    while True:
        command = input("What you want to do ? sum or sub or multiply or devide or modulas or reset or exit ")
        if command not in allowed:
            print("What are you doing man ? Have you eaten ganja??")
            for allow in allowed:
                print("Try ", allow)
            continue
        if command == "reset" :
            i = 0;
            for i in range(100):
                i += 1
            print("Resat in", i , "second")
            break
        if command == "sub":
            print("Substarcted value =", n1 - n2)
        if command == "sum":
            print("Sum of this two value is ", n1 + n2)
        if command == "multiply":
            print("Multiply of this two value is ", n1 * n2)
        if command == "devide":
            print("Devide of this two value is ", n1 / n2)
        if command == "modulas":
            print("Modulas of this two value is ", n1 % n2)
        if command == "exit":
            exit()