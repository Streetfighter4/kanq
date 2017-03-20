from django.conf.urls import url
from kanq_app.views import home
from kanq_app.views import images

urlpatterns = [
    url(r'^$', home.home_page, name='home'),
    url(r'^api/images/$', images.ImageList.as_view(), name='image_list')
]
