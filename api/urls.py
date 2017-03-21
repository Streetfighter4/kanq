from django.conf.urls import url

from api.views import images

urlpatterns = [
    url(r'^api/images/$', images.ImageList.as_view(), name='image_list')
]
