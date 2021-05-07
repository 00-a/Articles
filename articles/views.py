from django.shortcuts import render
from django.views.generic import TemplateView

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
