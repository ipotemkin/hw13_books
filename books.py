import json


class Books:

    def __init__(self, json_file):
        self.json_file = json_file
        self.max_id = 0
        self.books = []

    def read_json(self):
        with open(self.json_file, 'r', encoding='utf-8') as fp:
            try:
                self.books = json.load(fp)
                self.set_max_id()
            except:
                self.books = []
                self.max_id = 0

    def set_max_id(self):
        self.max_id = 0
        if self.books:
            for book in self.books:
                if book['id'] > self.max_id:
                    self.max_id = book['id']

    def to_json(self):
        with open(self.json_file, 'w', encoding='utf-8') as fp:
            json.dump(self.books, fp, ensure_ascii=False, indent='\t')

    def gen_isbn(self, number, name=""):
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
        new_book['id'] = self.max_id + 1
        new_book['isbn'] = self.gen_isbn(new_book['id'], new_book['name'])
        self.books.append(new_book)
        self.max_id += 1

    def remove_book_by_id(self, uid):
        book = self.get_book_by_id(uid)
        if book:
            self.books.remove(book)
            return True
        return False

    def get_book_by_id(self, uid):
        for book in self.books:
            if book['id'] == uid:
                return book
        return []

    def check_input(self, book):
        if book.get('name', "") and book.get('author', ""):
            return True
        return False

    def search(self, what: dict):
        # checking whether what is empty
        if not what:
            return []

        # checking whether no searching values - empty strings
        if len(''.join(what.values())) < 1:
            return []

        # genuine search
        # making case insensitive
        # using a new variable to not erase what for future needs
        new_what = {key.lower(): str(value).lower() for key, value in what.items()}

        # searching only all searching strings met
        results = []
        for book in self.books:
            results_line = {}
            for field in new_what.keys():
                if field in book.keys():
                    if new_what[field] in str(book[field]).lower():
                        results_line[field] = book[field]
            if len(results_line.keys()) == len(what.keys()):
                results.append(book)
        return results

    def __call__(self):
        return self.books
