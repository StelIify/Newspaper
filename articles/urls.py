from django.urls import path
from .views import ArticlesPageView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    CommentCreateView, UserArticlesListView

urlpatterns = [
    path('articles/', ArticlesPageView.as_view(), name='articles'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<str:username>', UserArticlesListView.as_view(), name='user_articles'),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='article_comment'),
]
