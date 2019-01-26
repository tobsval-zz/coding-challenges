#https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumerals:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.to_roman(arg)
        elif isinstance(arg, str):
            self.from_roman(arg)
        return None

    def to_roman(self, num : int):
        alphabet, str_num = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}, str(num)
        num_units, roman_number = [int(value) for value in str_num], str()
        num_units.sort()
        for exp in range(len(str_num)):
            num_units[exp] = num_units[exp] * (10 ** exp)
            if num_units[exp] in alphabet:
                roman_number += alphabet[num_units[exp]]
            elif num_units[exp] > 0: #Filter 0s
                self.find_order_of_magnitude(num_units[exp], list(alphabet.keys()))

    def from_roman(self, string : str):
        alphabet = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        pass

    def is_close_to_tens(self, number : int):
        #If a number is 1 unit away from a multiple of 10 it needs a special roman representation
        return True if number % 10 == 9 else False

    def find_order_of_magnitude(self, number : int, magnitudes : list):
        if len(str(number)) > len(str(max(magnitudes))): #In case a number is of a magnitude greater of 1000
            filtered_magnitudes = [1000]
        filtered_magnitudes = [num for num in magnitudes if len(str(num)) == len(str(number))]
        print(filtered_magnitudes)

#Work in Progress
