from django.test import TestCase, SimpleTestCase
from .models import Article, Comment
from accounts.models import CustomUser
from django.urls import reverse


class TestArticleViews(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="f0rest", email='morf268@ukr.net', password='12345')
        self.article = Article.objects.create(title='Intro to django', content="content about django", author=self.user)

    def test_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), reverse('articles'))

    def test_articles_page_view(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Intro to django')
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_articles_list_view_pagination(self):
        response = self.client.get('/articles/?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Intro to django')

    def test_article_detail_view(self):
        self.client.login(username="f0rest", password='12345')
        response = self.client.get(reverse('article_detail', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)



