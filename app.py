from flask import Flask, Response, request
from utils import *
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

BOOKS_FILE = 'books.json'


# to show all books
@app.route('/books/')
def get_all_books():
    books = read_json(BOOKS_FILE)
    return Response(json.dumps(books, ensure_ascii=False), content_type='application/json'), 200


# to show a book by id
@app.route('/books/<int:uid>')
def get_book(uid: int):
    books = read_json(BOOKS_FILE)
    book = get_book_by_id(uid, books)
    if not book:
        return Response(json.dumps({'error': 'Bad request'}), content_type='application/json'), 400
    return Response(json.dumps(book, ensure_ascii=False), content_type='application/json'), 200


# to create a book's record
@app.route('/books/', methods=['POST'])
def create_book():
    new_book = request.get_json()
    if not check_input(new_book):
        return Response(json.dumps({'error': 'Bad request'}), content_type='application/json'), 400
    books = read_json(BOOKS_FILE)
    new_id = create_new_id(books)
    new_book['id'] = new_id
    new_book['isbn'] = gen_isbn(new_id, new_book['name'])
    books.append(new_book)
    to_json(BOOKS_FILE, books)
    return Response(json.dumps(new_book, ensure_ascii=False), content_type='application/json'), 201


# to search a book's record
@app.route('/books/search/', methods=['GET'])
def search_book():
    what = dict(request.args)
    books = read_json(BOOKS_FILE)
    results = search2(what, books)
    if not results:
        return "", 204
    return Response(json.dumps(results, ensure_ascii=False), content_type='application/json'), 200


# to delete a book's record
@app.route('/books/<int:uid>', methods=['DELETE'])
def delete_book(uid: int):
    books = read_json(BOOKS_FILE)
    book = get_book_by_id(uid, books)
    if not book:
        return Response(json.dumps({'error': 'Not found'}), content_type='application/json'), 404
    books.remove(book)
    to_json(BOOKS_FILE, books)
    return Response(json.dumps({'status': 'Deleted'}, ensure_ascii=False), content_type='application/json'), 200


if __name__ == '__main__':
    app.run()
