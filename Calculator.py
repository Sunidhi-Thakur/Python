while True:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division\n")

    choice = int(input())
    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("\nSum of {} and {} = {}\n".format(a,b,a+b))
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("\nSubtracting {} from {} = {}\n".format(b,a,a-b))
    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("\nMultiplication of {} and {} = {}\n".format(a,b,a*b))
    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("\nDivision of {} by {} = {}\n".format(a,b,a/b))
    else:
        print("\nInvalid Input")
    
    count = input("\nDo you wish to continue [y/n] ")
    if count == 'n':
        break
