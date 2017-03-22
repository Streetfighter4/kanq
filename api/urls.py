from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views import posts
from api.views import images

router = DefaultRouter()

router.register(r'posts', posts.PostViewSet)
router.register(r'images', images.ImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
