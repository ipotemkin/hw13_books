from books import Books
from flask import Flask, Response, request
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
books = Books('books.json')
books.read_json()


# to show all books
@app.route('/books/')
def get_all_books():
    return Response(json.dumps(books(), ensure_ascii=False), content_type='application/json'), 200


# to show a book by id
@app.route('/books/<int:uid>')
def get_book(uid: int):
    book = books.get_book_by_id(uid)
    if not book:
        return Response(json.dumps({'error': 'Not found'}), content_type='application/json'), 404
    return Response(json.dumps(book, ensure_ascii=False), content_type='application/json'), 200


# to create a book's record
@app.route('/books/', methods=['POST'])
def create_book():
    new_book = request.get_json()
    if not books.check_input(new_book):
        return Response(json.dumps({'error': 'Bad request'}), content_type='application/json'), 400
    books.add_new_book(new_book)
    books.to_json()
    return Response(json.dumps(new_book, ensure_ascii=False), content_type='application/json'), 201


# to search a book's record
@app.route('/books/search/', methods=['GET'])
def search_book():
    results = books.search(dict(request.args))
    if not results:
        return "", 204
    return Response(json.dumps(results, ensure_ascii=False), content_type='application/json'), 200


# to delete a book's record
@app.route('/books/<int:uid>', methods=['DELETE'])
def delete_book(uid: int):
    if not books.remove_book_by_id(uid):
        return Response(json.dumps({'error': 'Not found'}), content_type='application/json'), 404
    books.to_json()
    return Response(json.dumps({'status': 'Deleted'}, ensure_ascii=False), content_type='application/json'), 200


if __name__ == '__main__':
# books = Books('books.json')
# books.read_json()
    app.run()
