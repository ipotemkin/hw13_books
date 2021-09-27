from flask import Flask, request
from utils import *


app = Flask(__name__)


BOOKS = []
BOOKS_FILE = 'books.json'


@app.route('/books/<uid>')
def get_book(uid):
    pass


@app.route('/create', methods=['POST'])
def create_book():
    book = request.get_json()
    books = read_json(BOOKS_FILE)
    if not books:
        id = 0


if __name__ == '__main__':
    # app.run()
    # print(gen_isbn(17))
    print(create_new_id([{'id': 10}]))
