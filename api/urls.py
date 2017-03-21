from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import images

router = DefaultRouter()
router.register(r'images', images.ImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
