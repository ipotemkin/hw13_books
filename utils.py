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


def gen_isbn(number, name=""):
    s1 = 978
    s2 = 1
    s3 = 266
    s4 = number  # 5 digits
    s5 = 1  # 1 digit (1-4) - control sum
    if name:
        s3 = int(str(abs(hash(name)))[:3])
    format_isbn = "%3s-%1s-%03d-%05d-%1s"
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
    if book.get('name', "") and book.get('author', ""):
        return True
    return False


# def search(word, field, books):
#     if not word:
#         return []
#     word = word.lower()
#     return [book for book in books if (field in book.keys()) and word in book[field].lower()]
#

def search2(what: dict, books):
    # checking whether what is empty
    if not what:
        return []

    # checking whether no searching values - empty strings
    if len(''.join(what.values())) < 1:
        return []

    # genuine search
    # making case insensitive
    # using a new variable to not erase what for future needs
    new_what = {key.lower(): str(value).lower() for key, value in what.items()}

    # searching only all searching strings met
    results = []
    for book in books:
        results_line = {}
        for field in new_what.keys():
            if field in book.keys():
                if new_what[field] in str(book[field]).lower():
                    results_line[field] = book[field]
        if len(results_line.keys()) == len(what.keys()):
            results.append(book)
    return results
