from rest_framework import serializers

from django_boilerplate.blog.models import BlogTag, BlogCategory, BlogPost, BlogImage
from django_boilerplate.common.drf_helpers.fields import RelatedField


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name', 'color']


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'created_at', 'updated_at']


class BlogImageSerializer(serializers.ModelSerializer):
    """
    Uploading Image:
    curl -x POST 'http://127.0.0.1:8000/api/blog/background-image/' \
        --form 'post="1"' \
        --form 'image=@"/Users/macbook/1.jpg"'
    Updating Image:
    curl -x PATCH 'http://127.0.0.1:8000/api/blog/background-image/1/' \
        --form 'image=@"/Users/macbook/2.jpg"'
    """

    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'image_width', 'image_height']


class BlogPostSerializer(serializers.ModelSerializer):
    category = RelatedField(
        BlogCategorySerializer, allow_null=True, required=False)
    tags = RelatedField(BlogTagSerializer, many=True)
    background_image = RelatedField(
        BlogImageSerializer, allow_null=True, required=False)

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'short_description', 'content', 'category', 'tags',
            'created_at', 'updated_at', 'background_image', 'status',
        ]
