from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views import posts

router = DefaultRouter()

router.register(r'posts', posts.PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
