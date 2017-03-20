from django.conf.urls import url
from kanq_app.views import home

urlpatterns = [
    url(r'^$', home.home_page, name='home'),
]
