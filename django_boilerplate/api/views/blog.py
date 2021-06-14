from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django_boilerplate.api.paginations import DefaultPagePagination
from django_boilerplate.blog.models import BlogImage, BlogCategory, BlogPost, BlogTag
from django_boilerplate.blog.serializers import (
    BlogTagSerializer,
    BlogCategorySerializer,
    BlogPostSerializer,
    BlogImageSerializer,
)
from django_boilerplate.common.drf_helpers.errors import BadRequestError
from django_boilerplate.common.drf_helpers.filters import key_filter, choices_filter
from django_boilerplate.common.drf_helpers.permissions import permission_builder
from django_boilerplate.common.drf_helpers.views import (
    ChoicesMixin,
    LabelsMixin,
    DictionaryMixin,
)


class BlogTagViewSet(ModelViewSet, DictionaryMixin):
    serializer_class = BlogTagSerializer
    queryset = BlogTag.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagePagination


class BlogCategoryViewSet(ModelViewSet, DictionaryMixin):
    serializer_class = BlogCategorySerializer
    queryset = BlogCategory.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagePagination
    filter_backends = [
        OrderingFilter,
    ]
    ordering_fields = ["created_at", "name"]

    def perform_destroy(self, instance):
        try:
            super().perform_destroy(instance)
        except models.ProtectedError:
            raise BadRequestError(_("You cannot delete category with existing posts"))


class BlogPostViewSet(ModelViewSet, ChoicesMixin, LabelsMixin, DictionaryMixin):
    model = BlogPost
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.distinct().all()
    permission_classes = [permission_builder()]
    filter_backends = [
        key_filter("tags"),
        key_filter("category"),
        choices_filter(BlogPost.Status, "status"),
        OrderingFilter,
        SearchFilter,
    ]
    ordering_fields = ["created_at", "updated_at"]
    search_fields = ["title", "short_description", "content"]
    pagination_class = DefaultPagePagination


class BlogImageViewSet(ModelViewSet):
    serializer_class = BlogImageSerializer
    queryset = BlogImage.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagePagination
