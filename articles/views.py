from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import CustomUser


class ArticlesPageView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'all_articles'
    paginate_by = 5
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Article
    template_name = 'articles/user_articles.html'
    context_object_name = 'user_articles'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username')) # get username from url
        return Article.objects.filter(author=user).order_by('-date_posted')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article_details.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'content']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'articles/comment_create.html'
    fields = ['comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs.get('pk')
        return super().form_valid(form)
