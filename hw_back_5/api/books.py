from fastapi import APIRouter, FastAPI, Form, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import jinja2
from ..repository.books import BooksRepository


books_router = APIRouter(prefix="/books", tags=["books"])
books_repo = BooksRepository()
templates = Jinja2Templates("hw_back_5/templates")



# (сюда писать решение)

@books_router.get("/new", response_class=HTMLResponse)
def show_add_books_form(request: Request):
    return templates.TemplateResponse("/books/new.html", {"request": request})


@books_router.get("/{id}", response_class=HTMLResponse)
def get_one(request: Request, id: int):
    book = books_repo.get_one(id)
    if not book:
        return Response("Not found", status_code=404, media_type="text/plain")
    return templates.TemplateResponse("/books/show.html", {"request": request, "book": book})


@books_router.get("/", response_class=HTMLResponse)
def get_books(request: Request, page: int = 1, per_page: int = 10):
    books = books_repo.get_all()
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


@books_router.post("/", response_class=HTMLResponse)
def add_book(request: Request, title: str = Form(...), author: str = Form(...), year: int = Form(...), total_pages: int = Form(...), genre: str = Form(...)):
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre
    }
    books_repo.save(new_book)

    return RedirectResponse(url="/books", status_code=303)

@books_router.get("/{id}/edit", response_class=HTMLResponse)
def edit_book(request: Request, id: int):
    book = books_repo.get_one(id)
    if not book:
        return Response("Not found", status_code=404, media_type="text/plain")
    return templates.TemplateResponse("/books/edit.html", {"request": request, "book": book})

@books_router.post("/{id}/edit", response_class=HTMLResponse)
def update_book(request: Request, id: int, title: str = Form(...), author: str = Form(...), year: int = Form(...), total_pages: int = Form(...), genre: str = Form(...)):
    book = books_repo.get_one(id)
    if not book:
        return Response("Not found", status_code=404, media_type="text/plain")
    book["title"] = title
    book["author"] = author
    book["year"] = year
    book["total_pages"] = total_pages
    book["genre"] = genre
    return RedirectResponse(url=f"/books/{id}", status_code=303)

@books_router.post("/{id}/delete", response_class=HTMLResponse)
def delete_book(request: Request, id: int):
    book = books_repo.get_one(id)
    if not book:
        return Response("Not found", status_code=404, media_type="text/plain")
    books_repo.delete(id)
    return RedirectResponse(url="/books", status_code=303)

@books_router.get("/{id}/delete", response_class=HTMLResponse)
def delete_book(request: Request, id: int):
    book = books_repo.get_one(id)
    if not book:
        return Response("Not found", status_code=404, media_type="text/plain")
    return templates.TemplateResponse("/books/delete.html", {"request": request, "book": book})

# (конец решения)
