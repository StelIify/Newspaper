from django.urls import path
from .views import SignUpView, LoginView, profile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile')
]