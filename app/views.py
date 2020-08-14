from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Article
from .serializers import ArticleSerializer


# Create your views here.
class ArticleViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['POST'], detail=False)
    def perform_create(self, serializer):
        return serializer.save()

    @action(methods=['PUT'], detail=True)
    def perform_update(self, serializer):
        serializer.save()

    @action(methods=['DELETE'], detail=True)
    def perform_destroy(self, instance):
        instance.delete()

