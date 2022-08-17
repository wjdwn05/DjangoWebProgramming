from django.urls import path
from  . import views 

app_name = 'bookmark'

urlpatterns = [
    path("",views.BookmarkLV.as_view(),name="bookmark_list"),
    path("<int:pk>/",views.BookmarkDV.as_view(),name="bookmark_detail"),
    path('add/',views.BookmarkCreateView.as_view(),name='add'),
    path('change/',views.BookmarkChangeLV.as_view(),name='change'),
    path('<int:pk>/update/',views.BookmarkUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',views.BookmarkDeleteView.as_view(),name='delete')

]
