from flask import Flask, Response, request
from utils import *
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

BOOKS_FILE = 'books.json'
USING_RAM = True  # to store all data in RAM in BOOKS
BOOKS = []


@app.route('/books/<int:uid>')
def get_book(uid: int):
    books = read_json(BOOKS_FILE) if not USING_RAM else BOOKS
    book = get_book_by_id(uid, books)
    print('get_book:')  # TODO remove
    print('books =', books)  # TODO remove
    print('BOOKS =', BOOKS)  # TODO remove
    print('BOOKS = books :', BOOKS is books)  # TODO remove
    if not book:
        return Response('Нет книги с таким кодом', content_type='text/http'), 400
    return Response(json.dumps(book, ensure_ascii=False), content_type='application/json'), 200
# в Safari вместо руссих букв вылазит абракадабра ((


@app.route('/create', methods=['POST'])
def create_book():
    global BOOKS
    new_book = request.get_json()
    if not check_input(new_book):
        return Response('Вы ввели %s. Введите книгу в формате {"name": "название", "author": "автор"}'
                        % json.dumps(new_book, ensure_ascii=False), content_type='text/http'), 400
    books = read_json(BOOKS_FILE) if not USING_RAM else BOOKS
    new_id = create_new_id(books)
    new_book['id'] = new_id
    new_book['isbn'] = gen_isbn(new_id, new_book['name'])
    books.append(new_book)
    # if USING_RAM:
    #     BOOKS = books
    to_json(BOOKS_FILE, books)
    print('create_book:')  # TODO remove
    print('books =', books)  # TODO remove
    print('BOOKS =', BOOKS)  # TODO remove
    print('BOOKS = books :', BOOKS is books)  # TODO remove
    return Response(json.dumps(new_book, ensure_ascii=False), content_type='application/json'), 201


@app.route('/search', methods=['POST'])
def search_book():
    books = read_json(BOOKS_FILE) if not USING_RAM else BOOKS
    what = request.get_json()
    results = search(list(what.values())[0], list(what.keys())[0], books)
    print('search_book:')  # TODO remove
    print('books =', books)  # TODO remove
    print('BOOKS =', BOOKS)  # TODO remove
    print('BOOKS = books :', BOOKS is books)  # TODO remove
    if not results:
        return Response('По запросу {} ничего не найдено'.format(json.dumps(what, ensure_ascii=False)),
                        content_type='text/http'), 400
    return Response(json.dumps(results, ensure_ascii=False), content_type='application/json'), 200
# в Safari вместо руссих букв вылазит абракадабра ((


@app.route('/delete/<int:uid>', methods=['DELETE'])
def delete_book(uid: int):
    books = read_json(BOOKS_FILE) if not USING_RAM else BOOKS
    book = get_book_by_id(uid, books)
    print('delete_book:')  # TODO remove
    print('books =', books)  # TODO remove
    print('BOOKS =', BOOKS)  # TODO remove
    print('BOOKS = books :', BOOKS is books)  # TODO remove
    if not book:
        return Response('Нет книги с таким кодом', content_type='text/http'), 400
    books.remove(book)
    to_json(BOOKS_FILE, books)
    return Response(json.dumps(book, ensure_ascii=False) + ' deleted', content_type='text/http'), 200


if __name__ == '__main__':
    if USING_RAM:
        BOOKS = read_json(BOOKS_FILE)
    app.run()

    # DEBUG
    # print(gen_isbn(17))
    # print(create_new_id([{'id': 10}]))

    # print(check_input({}))
    # print(check_input([]))
    # print(check_input({"name": "Name"}))
    # print(check_input({"name": "Name", "author": "Author"}))

    # print(hash("Конан Дойль"))
    # print(gen_isbn(1))
    # print(gen_isbn(1, "Конан Дойль"))
