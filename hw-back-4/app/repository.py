class BooksRepository:
    def __init__(self):
        self.books = [
            {
                "id": 1,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "total_pages": 336,
                "genre": "Fiction",
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "total_pages": 328,
                "genre": "Dystopian",
            },
            {
                "id": 3,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "total_pages": 180,
                "genre": "Classic",
            },
            {
                "id": 4,
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "total_pages": 1178,
                "genre": "Fantasy",
            },
            {
                "id": 5,
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "total_pages": 224,
                "genre": "Coming-of-age",
            },
            {
                "id": 6,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "total_pages": 336,
                "genre": "Fiction"
            },
            {
                "id": 7,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "total_pages": 328,
                "genre": "Dystopian"
            },
            {
                "id": 8,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "total_pages": 180,
                "genre": "Classic"
            },
            {
                "id": 9,
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "total_pages": 1178,
                "genre": "Fantasy"
            },
            {
                "id": 10,
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "total_pages": 224,
                "genre": "Coming-of-age"
            },
            {
                "id": 11,
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "year": 1813,
                "total_pages": 279,
                "genre": "Romance"
            },
            {
                "id": 12,
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "year": 1937,
                "total_pages": 310,
                "genre": "Fantasy"
            },
            {
                "id": 13,
                "title": "Moby-Dick",
                "author": "Herman Melville",
                "year": 1851,
                "total_pages": 635,
                "genre": "Adventure"
            },
            {
                "id": 14,
                "title": "War and Peace",
                "author": "Leo Tolstoy",
                "year": 1869,
                "total_pages": 1225,
                "genre": "Historical Fiction"
            },
            {
                "id": 15,
                "title": "The Alchemist",
                "author": "Paulo Coelho",
                "year": 1988,
                "total_pages": 208,
                "genre": "Philosophical Fiction"
            }
        ]

    def get_all(self):
        return self.books

    def get_one(self, id):
        # код писать сюда
        for book in self.books:
            if book['id'] == id:
                return book

        # конец
        return None

    def save(self, book):
        # код писать сюда
        book["id"] = len(self.books) + 1
        self.books.append(book)
        # конец
        return book
