from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer
from .forms import NewsForm, CommentForm

class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all().order_by('-created_at')
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

def news_list_view(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

class NewsDetailView(APIView):
    def get(self, request, news_id):
        news_item = get_object_or_404(News, id=news_id)
        serializer = NewsSerializer(news_item)
        return Response(serializer.data)

def news_detail_view(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    comments = news_item.comments.all().order_by('-created_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.save()
            return redirect('news_detail', news_id=news_id)
    else:
        form = CommentForm()
    return render(request, 'news/news_detail.html', {'news': news_item, 'comments': comments, 'form': form})

class AddNewsView(APIView):
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def add_news_view(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})