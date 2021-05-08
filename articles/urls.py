from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import MainPageView, ArticleDetailView, UserRegistrationView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainPage'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='articleDetail'),
    path('accounts/registration/', UserRegistrationView.as_view(), name='registration'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout')
]
