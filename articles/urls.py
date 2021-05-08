from django.urls import path
from .views import MainPageView, ArticleDetailView, UserRegistrationView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainPage'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='articleDetail'),
    path('accounts/registration/', UserRegistrationView.as_view(), name='registration'),
]
