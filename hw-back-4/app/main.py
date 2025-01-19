
from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .repository import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = BooksRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# (сюда писать решение)

@app.get("/books/new", response_class=HTMLResponse)
def show_add_books_form(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})


@app.get("/books/{id}", response_class=HTMLResponse)
def get_one(request: Request, id: int):
    book = repository.get_one(id)
    if not book:
        return Response("Not found", status_code=404, media_type="text/plain")
    return templates.TemplateResponse("/books/show.html", {"request": request, "book": book})


@app.get("/books", response_class=HTMLResponse)
def get_books(request: Request, page: int = 1, per_page: int = 10):
    books = repository.get_all()
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = books[start:end]
    
    next_page = page + 1 if end < len(books) else None
    previous_page = page - 1 if start > 0 else None

    return templates.TemplateResponse(
        "/books/index.html", 
        {
            "request": request,
            "books": [book for book in paginated_books],
            "next_page": next_page,
            "previous_page": previous_page,
            "per_page": per_page
        }
    )


@app.post("/books/new", response_class=HTMLResponse)
def add_car(request: Request, title: str = Form(...), author: str = Form(...), year: int = Form(...), total_pages: int = Form(...), genre: str = Form(...)):
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre
    }
    repository.save(new_book)

    return RedirectResponse(url="/books", status_code=303)
# (конец решения)
