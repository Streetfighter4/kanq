from django.conf.urls import url
from kanq_app import views

urlpatterns = [
    url(r'^$', views.home.home_page, name='home'),
]
