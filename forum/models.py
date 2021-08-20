from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    excerpt = models.CharField(max_length=200)
    text = models.TextField(max_length=500, null=False)
    slug = models.SlugField(max_length=50)
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='author')

    def __str__(self):
        return f'{ self.title }'

# Create your models here.
