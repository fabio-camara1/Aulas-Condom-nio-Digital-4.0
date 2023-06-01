def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


def vowel():
    vowel_counter = 0
    for x in text:
        if x in "aeiouAEIOU":
            vowel_counter += 1
    print(f"the number of vowel is {vowel_counter}")


def stock(amount, unitary_value):
    return amount * unitary_value


price = []
product = []


def add(a, b):
    price.append(a)
    product.append(b)
