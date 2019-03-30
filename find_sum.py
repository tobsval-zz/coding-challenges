"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def find_ksum(intarray, k):
	if intarray is None or k is None:
		return False
	else:
		needed_vals = {integer : k - integer for integer in intarray if integer > 0 or integer < k}
		for integer in intarray:
			if needed_vals[integer] in intarray:
				return True
		return False


# print(find_ksum([10, 3, 9, 8], 18))
