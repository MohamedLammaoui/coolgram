from django.urls import path
from .views import PostDetailView, PostFormView, PostListView, home

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post', PostFormView.as_view(), name="post"),
    path('posts/<slug:slug>', PostDetailView.as_view(), name="post-detail")
]
