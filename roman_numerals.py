# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumerals:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.to_roman(arg)
        elif isinstance(arg, str):
            self.from_roman(arg)
        return None

    def to_roman(self, num : int):
        alphabet, str_num = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}, str(num)
        num_units, roman_number = [int(value) for value in str_num][::-1], str()
        for exp in range(len(str_num)):
            num_units[exp] = num_units[exp] * (10 ** exp)
            if num_units[exp] in alphabet:
                roman_number += alphabet[num_units[exp]]
            elif num_units[exp] > 0: # Filter 0s
                self.find_magnitude_delta(num_units[exp], list(alphabet.keys()))

    def from_roman(self, string : str):
        alphabet = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        pass

    def find_magnitude_delta(self, number : int, magnitudes : list):
        if len(str(number)) > len(str(max(magnitudes))): # In case a number is of a magnitude greater than 1000
            filtered_magnitudes = [1000]
        filtered_magnitudes = [num for num in magnitudes if len(str(num)) == len(str(number))]
        # Calculate the offset between the number and the magnitude in order to find the closest one
        magnitude_deltas = list({mag : abs(number - mag) for mag in filtered_magnitudes}.values())
        print(magnitude_deltas)
        if magnitude_deltas[0] == magnitude_deltas[1]:
            print(number, min(magnitude_deltas))
        elif magnitude_deltas[0] > magnitude_deltas[1]:
            print(number, magnitude_deltas[1])
        else:
            print(number, magnitude_deltas[0])
        # WIP

RomanNumerals(543)

