#https://www.codewars.com/kata/does-my-number-look-big-in-this/train/python

def narcissistic(value):
    val = str(value)
    digits = [int(dig) for dig in val]
    num = sum(digit ** len(val) for digit in digits)
    return True if num == value else False

