from django.conf.urls import url
from api.views import home

urlpatterns = [
    url(r'^$', home.home_page, name='home'),
]
