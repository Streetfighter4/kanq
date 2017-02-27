from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', CreateView.as_view(
        template_name='registration/signup.html',
        form_class=UserCreationForm,
        success_url='/'
    )),
]