#https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(strng):
    weighted_nums_list = list()
    for weight in strng.split(' '):
        num_weight = sum(int(digit) for digit in weight) #Weight given by the sum of the digits
        weighted_nums_list.append((num_weight, weight))
        weighted_nums_list.sort(key = lambda tuple: tuple[0]) #Sorts based on the 'weight' of the number (first elem of the tuple)
    return ' '.join(weight[1] for weight in weighted_nums_list)

# TODO: Must implement lexicographical sorting in case of elements with same value

