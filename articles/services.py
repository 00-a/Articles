from articles.models import Article


def get_articles(**kwargs) -> 'QuerySet':
    return Article.objects.filter(**kwargs)


def create_or_update_article(form, request) -> None:
    article = form.save(commit=False)
    article.author = request.user
    article.save()
    form.save_m2m()


def get_context_from_articles(articles: 'QuerySet') -> dict:
    """Get article(s) if it exists, else get message"""
    return {'articles': articles} if articles else {'message': 'Article(s) does not exist(s)'}
