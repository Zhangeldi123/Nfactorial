from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import RedirectResponse, Response
from app.comments import Comment, CommentsRepository

app = FastAPI()
repo = CommentsRepository()

class CommentRequest(BaseModel):
    body: str
    category: str

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/comments", response_class=HTMLResponse)
def get_comments(request: Request, page: int = 1, per_page: int = 5):
    comments = repo.get_all()
    start = (page - 1) * per_page
    end = start + per_page
    paginated_comments = comments[start:end]
    

    next_page = page + 1 if end < len(comments) else None
    previous_page = page - 1 if start > 0 else None

    return templates.TemplateResponse(
        "pages/comments.html", 
        {
            "request": request,
            "comments": [comment.dict() for comment in paginated_comments],
            "next_page": next_page,
            "previous_page": previous_page,
            "per_page": per_page
        }
    )

@app.get("/add_comment", response_class=HTMLResponse)
def show_add_comment_form(request: Request):
    return templates.TemplateResponse("pages/opinion.html", {"request": request})

@app.post("/add_comment", response_class=HTMLResponse)
def add_comment(request: Request, body: str = Form(...), category: str = Form(...)):
    if category not in ["positive", "negative"]:
        return Response("Invalid category", status_code=400)
    
    new_comment = Comment(id=len(repo.comments) + 1, body=body, category=category)
    repo.save(new_comment)
    
    # Redirect to comments page after adding the comment
    return RedirectResponse(url="/comments", status_code=303)
