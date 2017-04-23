from django.db import models

# Create your models here.

class Article(models.Model):
    SOURCES = {
        ("MD","Medium"),
        ("GH","Github Trends"),
        ("RD","Reddit"),
        ("NY","NewY ork Times"),
    }
    idArticle = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    articleDate = models.DateTimeField()
    source = models.CharField(max_length=30,choices=SOURCES)
    creationDate = models.DateTimeField(auto_now=True)
