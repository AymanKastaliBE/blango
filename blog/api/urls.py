from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import PostList, PostDetail, UserDetail, PostViewSet
from rest_framework.authtoken import views


urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path(
        "posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)