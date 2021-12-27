from django.db import models
from django.http import request
from django.utils import timezone
from django.contrib.auth.models import User

from post.current_user import get_current_user


class Article(models.Model):
    author = models.ForeignKey(User,editable=False,default=get_current_user,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create your models here.
