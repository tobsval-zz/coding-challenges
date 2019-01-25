#https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

def anagrams(word, words):
    word_composition = { letter : word.count(letter) for letter in word}
    anagrams_list = []
    for _word in words:
        _word_comp = { letter : _word.count(letter) for letter in _word}
        if _word_comp == word_composition:
            anagrams_list.append(_word)
    return anagrams_list
