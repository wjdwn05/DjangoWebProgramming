from distutils.command.upload import upload
from email.mime import image
from django.db import models
from .fields import ThumbnailImageField
# Create your models here.

class Album(models.Model):
    name=models.CharField(max_length=50,verbose_name="앨범")
    description = models.CharField(max_length=100,verbose_name="앨범요약",blank=True)

class Photo(models.Model):
    album = models.ForeignKey(Album,on_delete= models.CASCADE)
    title = models.CharField(max_length=50,verbose_name='사진이름')
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField(blank=True,verbose_name='사진요약')
    upload_dt = models.DateTimeField(auto_now_add=True,verbose_name='업로드 시간')