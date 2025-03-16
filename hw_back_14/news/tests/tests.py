from django.test import TestCase
from django.urls import reverse
from news.models import News, Comment  # Import from actual models

class NewsModelTest(TestCase):
    def test_has_comments_true(self):
        news = News.objects.create(title="Test News", content="Some content")
        Comment.objects.create(news=news, content="Test comment")
        self.assertTrue(news.has_comments())

    def test_has_comments_false(self):
        news = News.objects.create(title="Test News", content="Some content")
        self.assertFalse(news.has_comments())

class NewsViewsTest(TestCase):
    def setUp(self):
        self.news1 = News.objects.create(title="News 1", content="Content 1")
        self.news2 = News.objects.create(title="News 2", content="Content 2")
        Comment.objects.create(news=self.news1, content="Comment 1")
        Comment.objects.create(news=self.news1, content="Comment 2")

    def test_news_list_sorted(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context['news'],
            News.objects.all().order_by('-created_at'),
            transform=lambda x: x
        )

    def test_news_detail(self):
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.news1.content)

    def test_news_comments_sorted(self):
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        self.assertEqual(response.status_code, 200)
        comments = response.context['comments']
        self.assertGreater(comments[0].created_at, comments[1].created_at)