from django.urls import path
from .views import PostFormView, home

urlpatterns = [
    path('', home, name="home"),
    path('post', PostFormView.as_view(), name="post"),
]
