import json


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        try:
            books = json.load(fp)
        except:
            books = []
        return books


def to_json(filename, books):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(books, fp, ensure_ascii=False, indent='\t')


def gen_isbn(number):
    s1 = 978
    s2 = 1
    s3 = 266
    s4 = number  # 5 digits
    s5 = 1  # 1 digit (1-4) - control sum
    format_isbn = "%3s-%1s-%3s-%05d-%1s"
    return format_isbn % (s1, s2, s3, s4, s5)


def create_new_id(books):
    if not books:
        return 1
    max_id = 0
    for book in books:
        if book['id'] > max_id:
            max_id = book['id']
    return max_id + 1


def get_book_by_id(uid, books):
    for book in books:
        if book['id'] == uid:
            return book
    return []


def check_input(book):
    if not book:
        print('1')
        return False
    try:
        if book['name'] and book['author']:
            print('2')
            return True
    except:
        print('3')
        return False
    return False
