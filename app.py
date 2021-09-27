from flask import Flask
import json

app = Flask(__name__)


BOOKS = []


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)


def to_json(filename, books):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(books, fp, ensure_ascii=False, indent='\t')


@app.route('/books/<uid>')
def get_book(uid):
    pass


@app.route('/', methods=['POST'])
def create_book(uid):
    pass


if __name__ == '__main__':
    app.run()
