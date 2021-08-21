from django.urls import path
from .views import PostDetailView, PostFormView, PostListView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', PostListView.as_view(), name="home-logged"),
    path('login/', auth_views.LoginView.as_view(template_name='forum/home.html'),  name="login"),
    path('post', PostFormView.as_view(), name="post"),
    path('posts/<slug:slug>', PostDetailView.as_view(), name="post-detail")
]
