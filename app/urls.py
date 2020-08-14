from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .views import ArticleViewSet

urlpatterns = [

]

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, base_name='app')

urlpatterns += router.urls