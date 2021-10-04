import json
from errors import ValidationError, NotFoundError


class Books:

    def __init__(self, json_file):
        self.json_file = json_file
        self.max_id = 0
        self.books = []

    def read_json(self):
        with open(self.json_file, 'r', encoding='utf-8') as fp:
            self.books = json.load(fp)
            self.set_max_id()

    def set_max_id(self):
        self.max_id = 0
        if self.books:
            for book in self.books:
                if book['id'] > self.max_id:
                    self.max_id = book['id']

    def to_json(self):
        with open(self.json_file, 'w', encoding='utf-8') as fp:
            json.dump(self.books, fp, ensure_ascii=False, indent='\t')

    @staticmethod
    def gen_isbn(number, name=""):
        s1 = 978
        s2 = 1
        s3 = 266
        s4 = number  # 5 digits
        s5 = 1  # 1 digit (1-4) - control sum
        if name:
            s3 = int(str(abs(hash(name)))[:3])
        format_isbn = "%3s-%1s-%03d-%05d-%1s"
        return format_isbn % (s1, s2, s3, s4, s5)

    def add_new_book(self, new_book):
        self.check_input(new_book)
        new_book['id'] = self.max_id + 1
        new_book['isbn'] = self.gen_isbn(new_book['id'], new_book['name'])
        self.books.append(new_book)
        self.max_id += 1

    def update(self, uid, new_book: dict):
        self.check_input(new_book)
        book = self.get_book_by_id(uid)
        book['name'] = new_book['name']
        book['author'] = new_book['author']

    def remove_book_by_id(self, uid):
        self.books.remove(self.get_book_by_id(uid))

    def get_book_by_id(self, uid):
        for book in self.books:
            if book['id'] == uid:
                return book
        raise IndexError

    @staticmethod
    def check_input(book):
        if book.get('name', "") and book.get('author', ""):
            return True
        raise ValidationError

    def search(self, what: dict):
        # checking whether what is empty or whether no searching values - empty strings
        if not what or not ''.join(what.values()):
            raise ValidationError

        # genuine search
        # making case insensitive
        # using a new variable to not erase what for future needs
        new_what = {key.lower(): str(value).lower() for key, value in what.items()}

        # searching only all searching strings met
        results = []
        for book in self.books:
            results_line = {field: book[field] for field in new_what.keys()
                            if field in book.keys() and (new_what[field] in str(book[field]).lower())}
            if len(results_line.keys()) == len(what.keys()):
                results.append(book)
        if results:
            return results
        raise NotFoundError

    def __call__(self, uid='all'):
        return self.books if uid == 'all' else self.get_book_by_id(uid)
