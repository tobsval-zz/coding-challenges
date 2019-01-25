#https://www.codewars.com/kata/the-hashtag-generator/python

def generate_hashtag(s):
    camel_case_word = ''.join([word.capitalize() for word in s.split()])
    if len(camel_case_word) >= 140 or s == '':
        return False
    return '#' + camel_case_word
    
