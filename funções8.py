def quantity_letters():
    text = input("type the text:")
    print(len(text) - text.count(" "))
    print(f"{text[::-1]}")


quantity_letters()
