from django.urls import path
from .views import MainPageView, ArticleDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='mainPage'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='articleDetail'),
]