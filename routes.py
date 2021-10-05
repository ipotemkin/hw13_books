from __init__ import *
from books import Books
from flask import Flask, jsonify, request
from errors import ValidationError, NotFoundError


@app.errorhandler(IndexError)
def not_found_error(error: IndexError):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(ValidationError)
def bad_request_error(error: ValidationError):
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(NotFoundError)
def bad_request_error(error: NotFoundError):
    return '', 204


# to show all books
@app.route('/books/')
def get_all_books():
    books.read_json()
    return jsonify(books())


# to show a book by id
@app.route('/books/<int:uid>')
def get_book(uid: int):
    books.read_json()
    return jsonify(books(uid))


# to create a book's record
@app.route('/books/', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.read_json()
    books.add_new_book(new_book)
    books.to_json()
    return jsonify(new_book), 201


# to search a book's record
@app.route('/books/search/', methods=['GET'])
def search_book():
    books.read_json()
    return jsonify(books.search(dict(request.args)))


# to delete a book's record
@app.route('/books/<int:uid>', methods=['DELETE'])
def delete_book(uid: int):
    books.read_json()
    books.remove_book_by_id(uid)
    books.to_json()
    return jsonify({'status': 'Deleted'})


# to update a book's record
@app.route('/books/<int:uid>', methods=['PUT'])
def update_book(uid: int):
    books.read_json()
    books.update(uid, request.get_json())
    books.to_json()
    return jsonify(books(uid))
