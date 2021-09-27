from flask import Flask, request
import json

app = Flask(__name__)


BOOKS = []
BOOKS_FILE = 'books.json'


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)


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


@app.route('/books/<uid>')
def get_book(uid):
    pass


@app.route('/create', methods=['POST'])
def create_book():
    book = request.get_json()
    books = read_json(BOOKS_FILE)
    if not books:
        id = 0


    pass


if __name__ == '__main__':
    # app.run()
    # print(gen_isbn(17))
    print(create_new_id([{'id': 10}]))
