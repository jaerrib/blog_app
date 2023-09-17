from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("blog_base/", views.PostList.as_view(), name="blog_index"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
