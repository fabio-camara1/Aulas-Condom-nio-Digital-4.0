def addition():
    print(number1 + number2)


def subtraction():
    print(number1 - number2)


def multiplication():
    print(number1 * number2)


def division():
    print(number1 / number2)


while True:
    number1 = int(input("put fist number:"))
    number2 = int(input("put second number"))
    menu = input("which operation you want to apply 1-addition, 2-subtraction, 3-multiplication, 4-division, 5-exit ")
    if menu == "1":
        addition()
    elif menu == "2":
        subtraction()
    elif menu == "3":
        multiplication()
    elif menu == "4":
        division()
    elif menu == "5":
        break
    else:
        print("enter a valid option")
        continue
    again = input("what to repeat the program y-yes, n-no")
    if again == "y":
        continue
    elif again == "n":
        break
    else:
        print("enter a valid option")
