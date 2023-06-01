text = "the mouse gnawed the clothes of king of rome"


def vowel():
    vowel_counter = 0
    for x in text:
        if x in "aeiouAEIOU":
            vowel_counter += 1
    print(f"the number of vowel is {vowel_counter}")


vowel()
