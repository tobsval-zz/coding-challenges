#https://www.codewars.com/kata/does-my-number-look-big-in-this/train/python

def narcissistic(value):
    digits = [int(dig) for dig in str(value)]
    num = sum(digit ** len(str(value)) for digit in digits)
    return True if num == value else False
