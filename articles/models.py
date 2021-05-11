from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articleDetail", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Tag(models.Model):
    """Tag for article"""
    name = models.CharField(max_length=50, verbose_name="Tag name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Comment(models.Model):
    """Comment for article"""

    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='article')
    text = models.TextField(max_length=1000, verbose_name='comment_text')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='comment_author')
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
