from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from attrs import define
import json

app = FastAPI()

class Comment(BaseModel):
    body: str
    category: str
    id: int | None = None


class CommentsRepository:

    def __init__(self):
        self.comments = [
            Comment(body="Wish you all good luck!", category="Positive", id = 1),
            Comment(body="Wish you all bad luck!", category="Negative", id = 2),
            Comment(body="The cake is a lie!", category="Negative", id = 3)
        ]

    def get_all(self):
        return self.comments

    def save(self, comment: Comment):
        comment.id = len(self.comments) + 1
        self.comments.append(comment)
        return comment

