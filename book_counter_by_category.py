#https://www.codewars.com/kata/help-the-bookseller/train/python

def stock_list(list_of_art, list_of_cat):
    category_dict = dict().fromkeys(list_of_cat, 0)
    for book in list_of_art:
        if book[0] in category_dict:
            category_dict[book[0]] += int(book.split(' ')[1])
        category_dict[book[0]] = int(book.split(' ')[1])
    return category_dict

