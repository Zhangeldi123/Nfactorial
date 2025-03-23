from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer
from .forms import NewsForm, CommentForm, SignUpForm
from django.views import View
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return HttpResponseForbidden("Вы не можете удалить этот комментарий.")
    
    news_id = comment.news.id
    comment.delete()
    return redirect('news_detail', news_id=news_id)


@login_required
def delete_news_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.user != news.author:
        return HttpResponseForbidden("Вы не можете удалить эту новость.")
    
    news.delete()
    return redirect('news_list')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/login/')
        else:
            print(form.errors)  # Показываем ошибки формы
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', {'form': form})



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
    
    is_moderator = request.user.groups.filter(name='moderators').exists() if request.user.is_authenticated else False

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.author = request.user
            comment.save()
            return redirect('news_detail', news_id=news_id)
    else:
        form = CommentForm()
    
    return render(request, 'news/news_detail.html', {
        'news': news_item,
        'comments': comments,
        'form': form,
        'is_moderator': is_moderator,
    })



class AddNewsView(APIView):
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='/auth/login/')  # Перенаправляет на страницу логина, если не авторизован
def add_news_view(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

#django part 4 hw
class NewsUpdateView(View):
    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        form = NewsForm(instance=news)
        return render(request, 'news/news_form.html', {'form': form})

    def post(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect(f'/news/{pk}/')
        return render(request, 'news/news_form.html', {'form': form})