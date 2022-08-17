from mysite.views import OwnerOnlyMixin
from bookmark.models import Bookmark
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy


class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin,CreateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:bookmark_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin,ListView):
    template_name = "bookmark/changelist.html"
    def get_queryset(self):
        return Bookmark.objects.filter(owner = self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin,UpdateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:bookmark_list')

class BookmarkDeleteView(OwnerOnlyMixin,DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:bookmark_list')
