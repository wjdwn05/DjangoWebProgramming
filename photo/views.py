from django.shortcuts import redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Album,Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from .forms import PhotoInlineFormSet
# Create your views here.
class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo
class PhotoCV(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ('album','title','description','image')
    success_url = reverse_lazy('photo:index')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
class PhotoChangeLV(LoginRequiredMixin,ListView):
    model = Photo
    template_name = 'photo/photochangelist.html'
    def get_queryset(self):
        return Photo.objects.filter(owner = self.request.user)
class PhotoUV(OwnerOnlyMixin,UpdateView):
    model = Photo
    fields = ('album','title','description','image')
    success_url = reverse_lazy('photo:index')
class PhotoDelV(OwnerOnlyMixin,DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')
class AlbumChangeLV(LoginRequiredMixin,ListView):
    model = Album
    template_name = 'photo/albumchangelist.html'
    def get_queryset(self):
        return Photo.objects.filter(owner = self.request.user) 
class AlbumUV(OwnerOnlyMixin,UpdateView):
    model = Album
    fields = ('name','description')
    success_url = reverse_lazy('photo:index')
class AlbumDelV(OwnerOnlyMixin,DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')
class AlbumPhotoCV(LoginRequiredMixin,CreateView):
    model = Album
    fields = ('name','description')
    success_url = reverse_lazy('photo:index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(OwnerOnlyMixin, UpdateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))