from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    MainPageView,
    ArticleDetailView,
    UserRegistrationView,
    AllArticlesByUserView,
    NewArticleView,
    EditArticleView,
    DeleteArticleView
)


urlpatterns = [
    path('', MainPageView.as_view(), name='mainPage'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='articleDetail'),
    path('article/new', NewArticleView.as_view(), name='newArticle'),
    path('article/<int:pk>/edit/', EditArticleView.as_view(), name='articleEdit'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(), name='articleDelete'),
    path('user/<slug:slug_username>/articles', AllArticlesByUserView.as_view(), name='allArticlesByUser'),
    path('accounts/registration/', UserRegistrationView.as_view(), name='registration'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout')
]
