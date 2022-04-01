from django.test import TestCase, SimpleTestCase
from .models import Article, Comment
from accounts.models import CustomUser
from django.urls import reverse


class TestArticleViews(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="f0rest", email='morf268@ukr.net', password='12345')
        self.article = Article.objects.create(title='Intro to django', content="content about django", author=self.user)
        second_user = CustomUser.objects.create_user(username="stellify", email="morf3310@gmail.com", password='54321')
        Article.objects.create(title='Intro to Flask', content="content about Flask", author=second_user)

    def test_absolute_url(self):  # move to model test
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

    def test_user_articles_list_view(self):
        response = self.client.get(reverse('user_articles', kwargs={'username': self.article.author.username}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Intro to django")
        self.assertNotContains(response, "Intro to Flask")

    def test_article_detail_view(self):
        self.client.login(username="f0rest", password='12345')
        response = self.client.get(reverse('article_detail', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_details.html')
        self.assertContains(response, self.article.content)

    def test_article_create_view(self):
        response = self.client.post(reverse('article_new'), {
            'title': 'Intro to FastAPI',
            'content': 'content about FastAPI',
            'author': self.user
        })

        self.assertEqual(response.status_code, 302)
