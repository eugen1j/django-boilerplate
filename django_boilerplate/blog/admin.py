from django.contrib import admin

from django_boilerplate.blog.models import BlogTag, BlogCategory, BlogPost, BlogImage


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    ordering = ['updated_at']


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    ordering = ['updated_at']


class BlogImageAdmin(admin.ModelAdmin):
    list_display = ['image']


admin.site.register(BlogTag, BlogTagAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
