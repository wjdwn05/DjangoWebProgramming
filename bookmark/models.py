from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=100,verbose_name="즐겨찾기 제목",blank=True)
    url = models.URLField(unique=True,verbose_name="즐겨찾기 URL")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank= True, null= True)