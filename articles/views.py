from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from articles.forms import RegistrationForm
from articles.services import get_articles, get_context_from_articles


class MainPageView(TemplateView):
    """Main page. All articles on the site"""
    template_name = 'articles/main_page.html'

    def get(self, request):
        articles = get_articles()
        return render(request, self.template_name, get_context_from_articles(articles))


class ArticleDetailView(TemplateView):
    """Full text of the article"""
    template_name = 'articles/article_detail.html'

    def get(self, request, pk):
        article = get_articles(pk=pk)
        return render(request, self.template_name, get_context_from_articles(article))


class UserRegistrationView(TemplateView):
    """New user registration"""
    template_name = 'registration/registration.html'

    def get(self, request):
        form = RegistrationForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainPage')
        context = {'form': form}
        return render(request, self.template_name, context)
