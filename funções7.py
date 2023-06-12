from funcoes import *

while True:
    argument = input("enter product name:")
    argument2 = int(input("enter the price:"))
    add(argument, argument2)
    repeat = input("want to add more products y- yes, n- no")
    if repeat == "y":
        print("okay")
    elif repeat == "n":
        print("okay")
        break
    else:
        print("enter a valid option")

print(price)
print(product)
