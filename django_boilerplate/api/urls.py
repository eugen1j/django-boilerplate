from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django_boilerplate.api.views import user, auth, blog

router = DefaultRouter()
router.register("user", user.UserViewSet)
router.register("blog/tag", blog.BlogTagViewSet)
router.register("blog/post", blog.BlogPostViewSet)
router.register("blog/category", blog.BlogCategoryViewSet)
router.register("blog/image", blog.BlogImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login/", auth.LoginView.as_view()),
    path("auth/user/", auth.UserView.as_view()),
    path("auth/refresh/", auth.RefreshView.as_view()),
    path("auth/logout/", auth.LogoutView.as_view()),
]
