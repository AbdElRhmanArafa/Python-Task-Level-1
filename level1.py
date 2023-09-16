#!/usr/bin/python3
"""
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
"""


def odd_even(x, y):
    odd = []
    even = []
    for num in range(x, y + 1):
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd


"""
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y
"""


def divided_on_X_Y(x, y):
    divided = []
    for num in range(1, 101):
        if num % x == 0 and num % y == 0:
            divided.append(num)
    return divided


"""
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
"""


def multiplication_table(x, y):
    for num1 in range(x, y + 1):
        for num2 in range(1, 13):
            result = num1 * num2
            print(f"{num1} x {num2} = {result}")
        print("=" * 15)


"""
Create a function that takes a sentence and prints the sentence without duplicated words 
"""

def no_duplicated(sentence = ""):
    list_sentence = sentence.split(' ')
    clean_sentece =[]
    for word in list_sentence:
        if word not in clean_sentece:
            clean_sentece.append(word)
    print(clean_sentece)

