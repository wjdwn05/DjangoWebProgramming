from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

admin.site.register(Bookmark,BookmarkAdmin)