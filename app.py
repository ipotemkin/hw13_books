from flask import Flask, Response, request
from utils import *
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

BOOKS_FILE = 'books.json'
HTML_WRAP = '<html lang="ru"><meta charset="UTF-8"><p>{}</p></html>'


@app.route('/books/<int:uid>')
def get_book(uid: int):
    books = read_json(BOOKS_FILE)
    book = get_book_by_id(uid, books)
    if not book:
        return Response(HTML_WRAP.format('Нет книги с таким кодом'), content_type='text/html'), 400
    return Response(json.dumps(book, ensure_ascii=False), content_type='application/json'), 200
# в Safari вместо руссих букв вылазит абракадабра ((


@app.route('/create', methods=['POST'])
def create_book():
    new_book = request.get_json()
    if not check_input(new_book):
        message = 'Вы ввели {}. Введите книгу в формате {"name": "название", "author": "автор"}'
        message = message.format(json.dumps(new_book, ensure_ascii=False))
        return Response(HTML_WRAP.format(message), content_type='text/html'), 400
    books = read_json(BOOKS_FILE)
    new_id = create_new_id(books)
    new_book['id'] = new_id
    new_book['isbn'] = gen_isbn(new_id, new_book['name'])
    books.append(new_book)
    to_json(BOOKS_FILE, books)
    return Response(json.dumps(new_book, ensure_ascii=False), content_type='application/json'), 201


@app.route('/search', methods=['POST'])
def search_book():
    books = read_json(BOOKS_FILE)
    what = request.get_json()
    results = search(list(what.values())[0], list(what.keys())[0], books)
    if not results:
        return Response('По запросу {} ничего не найдено'.format(json.dumps(what, ensure_ascii=False)),
                        content_type='text/html'), 400
    return Response(json.dumps(results, ensure_ascii=False), content_type='application/json'), 200
# в Safari вместо руссих букв вылазит абракадабра на месте json ((


@app.route('/delete/<int:uid>', methods=['DELETE'])
def delete_book(uid: int):
    books = read_json(BOOKS_FILE)
    book = get_book_by_id(uid, books)
    if not book:
        return Response(HTML_WRAP.format('Нет книги с таким кодом'), content_type='text/html'), 400
    books.remove(book)
    to_json(BOOKS_FILE, books)
    return Response(json.dumps(book, ensure_ascii=False) + ' deleted', content_type='text/html'), 200


if __name__ == '__main__':
    app.run()
