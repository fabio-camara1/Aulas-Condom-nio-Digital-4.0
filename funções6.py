argument = int(input("enter a number"))


def positive():
    if argument > 0:
        print("p")
    elif argument < 0:
        print("n")
    elif argument == 0:
        print("z")


positive()
