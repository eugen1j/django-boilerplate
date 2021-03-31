from django.contrib import admin

from django_boilerplate.blog.models import BlogTag, BlogCategory, BlogPost, BackgroundImage


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    ordering = ['updated_at']


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    ordering = ['updated_at']


class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']


admin.site.register(BlogTag, BlogTagAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)
