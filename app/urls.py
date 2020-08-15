from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import ArticleViewSet

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, base_name='app')

urlpatterns += router.urls