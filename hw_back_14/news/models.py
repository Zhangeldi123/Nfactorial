from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        default=1  # Указываем ID существующего пользователя
    )

    def has_comments(self):
        return self.comments.exists()

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        default=1  # Указываем ID существующего пользователя
    )

    def __str__(self):
        return f'Comment on {self.news.title}'