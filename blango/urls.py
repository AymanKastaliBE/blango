from django.contrib import admin
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("api/v1/", include("blog.api.urls")),
]
