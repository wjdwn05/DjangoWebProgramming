from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import AccessMixin
class Homeview(TemplateView):
    template_name = "home.html"

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = '이 글의 주인만 삭제 또는 수정할 수 있습니다'
    def dispatch(self,request,*args,**kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request,*args,**kwargs)
