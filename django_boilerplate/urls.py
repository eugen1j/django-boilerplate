"""project URL Configuration"""
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from django_boilerplate.settings import DEBUG, MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path("api/", include("django_boilerplate.api.urls")),
    path("admin/", admin.site.urls),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
