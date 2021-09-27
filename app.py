from flask import Flask, Response, request
from utils import *


app = Flask(__name__)


BOOKS = []
BOOKS_FILE = 'books.json'


@app.route('/books/<int:uid>')
def get_book(uid: int):
    books = read_json(BOOKS_FILE)
    print(books)
    book = get_book_by_id(uid, books)
    return Response(json.dumps(book), content_type='application/json'), 200


@app.route('/create', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books = read_json(BOOKS_FILE)
    new_id = create_new_id(books)
    new_book['id'] = new_id
    new_book['isbn'] = gen_isbn(new_id)
    books.append(new_book)
    to_json(BOOKS_FILE, books)
    # print(books)  # TODO remove
    return Response(json.dumps(new_book), content_type='application/json'), 201


if __name__ == '__main__':
    app.run()
    # print(gen_isbn(17))
    # print(create_new_id([{'id': 10}]))
