from distutils.command.upload import upload
from email.mime import image
from django.db import models
from .fields import ThumbnailImageField
from django.urls import reverse
# Create your models here.

class Album(models.Model):
    name=models.CharField(max_length=50,verbose_name="앨범")
    description = models.CharField(max_length=100,verbose_name="앨범요약",blank=True)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,blank=True,null=True)
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))
class Photo(models.Model):
    album = models.ForeignKey(Album,on_delete= models.CASCADE)
    title = models.CharField(max_length=50,verbose_name='사진이름')
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField(blank=True,verbose_name='사진요약')
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,blank=True,null=True)
    upload_dt = models.DateTimeField(auto_now_add=True,verbose_name='업로드 시간')
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
    

