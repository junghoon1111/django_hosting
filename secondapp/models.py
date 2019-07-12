# Create your models here.
'''from django.db import models
from django.utils import timezone

class Post(models.Model):
    aurthor = models.Foreignkey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_lenghth=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    )
'''