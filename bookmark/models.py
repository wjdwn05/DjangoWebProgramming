from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=100,verbose_name="즐겨찾기 제목",blank=True)
    url = models.URLField(unique=True,verbose_name="즐겨찾기 URL")