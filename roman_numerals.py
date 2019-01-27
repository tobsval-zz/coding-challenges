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
        num_digits, roman_num = [int(value) for value in str_num][::-1], str()
        for exp in range(len(str_num)):
            num_digits[exp] = num_digits[exp] * (10 ** exp)
            if num_digits[exp] in alphabet:
                roman_num += alphabet[num_digits[exp]]
            elif num_digits[exp] > 0: # Filter 0s
                closest_mag = self.find_closest_magnitude(num_digits[exp], list(alphabet.keys()))
                print(closest_mag)

    def from_roman(self, string : str):
        alphabet = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        pass

    def find_closest_magnitude(self, number : int, magnitudes : list):
        # In case a number is of a magnitude greater than 1000 or is a multiple of 1000
        if len(str(number)) > len(str(max(magnitudes))) or number % 1000 == 0:
            return 1000
        filtered_magnitudes = [num for num in magnitudes if len(str(num)) == len(str(number))]
        # Calculate the offset between the number and the magnitude in order to find the closest one
        magnitude_deltas = list({mag : abs(number - mag) for mag in filtered_magnitudes}.values())
        if magnitude_deltas[0] == magnitude_deltas[1]:
            return min(filtered_magnitudes)
        elif magnitude_deltas[0] > magnitude_deltas[1]:
            return filtered_magnitudes[1]
        else:
            return filtered_magnitudes[0]
        # WIP

RomanNumerals(543)

