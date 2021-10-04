BOOKS Storage
===

A simple web API application - finishing Module 2 of PD
---

Functions realized:
---

> Get all books
>> `GET /books/`
> ```json
> [{
>  "author": "Джоан Роулинг", 
>  "id": 1, 
>  "isbn": "978-1-266-00001-1", 
>  "name": "Гарри Потер"
> },
> {
>  "name": "Гарри Потер",
>  "author": "Джоан Роулинг",
>  "id": 2,
>  "isbn": "978-1-266-00002-1"
> }]
>```



> Get a book by ID
>> `GET /books/ID`
> ```json
> {
>  "author": "Джоан Роулинг", 
>  "id": 1, 
>  "isbn": "978-1-266-00001-1", 
>  "name": "Гарри Потер"
> }
>```

> Create a book
>> `POST /books/`
> ```json
> {
>  "author": "Джоан Роулинг", 
>  "name": "Гарри Потер"
> }
>```

> Find a book
>> `GET /books/search/?name=потер&author=`
> ```json
> {
>  "author": "Джоан Роулинг", 
>  "id": 1, 
>  "isbn": "978-1-266-00001-1", 
>  "name": "Гарри Потер"
> }
>```

> Delete a book by ID
>> `DELETE /books/ID`
> ```json
> {
>  "author": "Джоан Роулинг", 
>  "id": 1, 
>  "isbn": "978-1-266-00001-1", 
>  "name": "Гарри Потер"
> }
>```

> Update a book
>> `PUT /books/ID`
> ```json
> {
>  "author": "Джоан Роулинг", 
>  "name": "Гарри Потер"
> }
>```
