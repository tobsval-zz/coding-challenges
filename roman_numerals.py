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
                if closest_mag > num_digits[exp]:
                    pass #WIP
                else:
                    pass #WIP
        return roman_num

    def from_roman(self, string : str):
        alphabet = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        pass

    def find_closest_magnitude(self, number : int, magnitudes : list):
        if number % 1000 == 0:
            return 1000
        elif number % 5 == 1:
            filtered_magnitudes = [num for num in magnitudes if (num - number) <= (num / 100) * 10]
        else:
            filtered_magnitudes = [num for num in magnitudes if (num - number) <= (num / 100) * 20]
        # Calculate the offset between the number and the magnitude in order to find the closest one
        magnitude_deltas = [abs(number - mag) for mag in filtered_magnitudes]
        minimum_delta = magnitude_deltas.index(min(magnitude_deltas))
        return filtered_magnitudes[minimum_delta]


RomanNumerals(5)

