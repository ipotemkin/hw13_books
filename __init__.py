from flask import Flask
from books import Books
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['JSON_AS_ASCII'] = False
books = Books('books.json')
