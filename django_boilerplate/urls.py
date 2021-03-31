"""project URL Configuration"""
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from django_boilerplate.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

# from rest_framework_jwt.settings import api_settings
#
# if api_settings.JWT_AUTH_COOKIE:
#     from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#     from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
#     from rest_framework_jwt.views import RefreshJSONWebToken
#
#     RefreshJSONWebTokenSerializer._declared_fields.pop('token')
#
#     class RefreshJSONWebTokenSerializerCookieBased(RefreshJSONWebTokenSerializer):
#         def validate(self, attrs):
#             if 'token' not in attrs:
#                 if api_settings.JWT_AUTH_COOKIE:
#                     attrs['token'] = JSONWebTokenAuthentication().get_jwt_value(self.context['request'])
#             return super(RefreshJSONWebTokenSerializerCookieBased, self).validate(attrs)
#
#     RefreshJSONWebToken.serializer_class = RefreshJSONWebTokenSerializerCookieBased

urlpatterns = [
    path('api/', include('django_boilerplate.api.urls')),
    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
