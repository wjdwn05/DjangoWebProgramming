from tabnanny import verbose
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name='제목')
    slug = models.SlugField(max_length=50,unique=True,verbose_name='슬러그',allow_unicode=True)
    description = models.CharField(max_length=100,blank=True,verbose_name='요약')
    content = models.TextField(verbose_name='본문')
    create_dt = models.DateTimeField(auto_now_add=True,verbose_name='작성일')
    modify_dt = models.DateTimeField(auto_now=True,verbose_name='수정일')
    tags = TaggableManager( blank=True,verbose_name="태그")

    class Meta():
        verbose_name = '포스트'
        verbose_name_plural = '포스트'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
