from flask import Flask, request
import json

app = Flask(__name__)


BOOKS = []


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


@app.route('/books/<uid>')
def get_book(uid):
    pass


@app.route('/create', methods=['POST'])
def create_book():
    book = request.get_json()

    pass


if __name__ == '__main__':
    # app.run()
    print(gen_isbn(17))
