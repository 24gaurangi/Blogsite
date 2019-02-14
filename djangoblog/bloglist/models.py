from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    description=models.TextField()
    likes=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png', blank=True)
    author=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    #thumbnail author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50]+"..."


class Comment(models.Model):
    blog=models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    comment=models.CharField(max_length=255)
    # upvote=models.IntegerField()
    # downvote=models.IntegerField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment