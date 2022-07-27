from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=1000, default="")
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)

