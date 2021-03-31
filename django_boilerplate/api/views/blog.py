from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django_boilerplate.api.paginations import DefaultPagePagination
from django_boilerplate.blog.models import BackgroundImage, BlogCategory, BlogPost, BlogTag
from django_boilerplate.blog.serializers import BlogTagSerializer, BlogCategorySerializer, \
    BlogPostSerializer, BackgroundImageSerializer


class BlogTagViewSet(ModelViewSet):
    serializer_class = BlogTagSerializer
    queryset = BlogTag.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagePagination


class BlogCategoryViewSet(ModelViewSet):
    serializer_class = BlogCategorySerializer
    queryset = BlogCategory.objects.all()
    pagination_class = DefaultPagePagination


class BlogPostViewSet(ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    pagination_class = DefaultPagePagination


class BackgroundImageViewSet(ModelViewSet):
    serializer_class = BackgroundImageSerializer
    queryset = BackgroundImage.objects.all()
    pagination_class = DefaultPagePagination
