from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import include, path, reverse

from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from .models import Article


class ArticleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        testuser1 = User.objects.create_user(
            username='testuser1', 
            password='abc123'
        )
        testuser1.save()

        test_post = Article.objects.create(
            author= testuser1,
            title='Test Article', 
            body='Test', 
            cover_photo="test.jpg"
        )
        test_post.save()

    def test_article_content(self):
        article = Article.objects.get(id=1)
        title = f'{article.title}'
        body = f'{article.body}'
        cover_photo = f'{article.cover_photo}'
        author = f'{article.author}'
        self.assertEqual(title, 'Test Article')
        self.assertEqual(body, 'Test')
        self.assertEqual(cover_photo, 'test.jpg')
        self.assertEqual(author, 'testuser1')


class ArticleAPITests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('blog/', include('blog.urls')),
    ]

    def test_article_list_api(self):
        url = reverse('article-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_detail_api_fail(self):
        url = reverse('article-detail', kwargs={'slug': 'test'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)