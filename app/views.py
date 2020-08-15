from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

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
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    @action(methods=['POST'], detail=False)
    def perform_create(self, serializer):
        return serializer.save()

    @action(methods=['PUT'], detail=True)
    def perform_update(self, serializer):
        serializer.save()

    @action(methods=['DELETE'], detail=True)
    def perform_destroy(self, instance):
        instance.delete()

    def get(self):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

