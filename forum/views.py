from django.conf.urls import url
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm
from .models import Post

from slugify import slugify

class PostDetailView(DetailView):
    template_name = 'forum/single_post.html'
    model = Post
    context_object_name = 'post'

class PostListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'forum/home.html'
    model = Post
    paginate_by = 10
    context_object_name = 'posts'

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    

class PostFormView(FormView):
    template_name = 'forum/post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            try:
                title = form.cleaned_data['title']
                message = form.cleaned_data['message']
                image = form.cleaned_data['image']
                excerpt = message[0:200] + "..."
                slug = slugify(title)
                user = self.request.user

                post = Post(title=title, message=message, excerpt=excerpt, slug=slug, user=user, image=image)

                post.save()

                return render(self.request, "forum/home.html")

            except:
                print("Couldn't save into Post model")

        return render(self.request, "forum/post.html", {
            "form": form
        })
# Create your views here.
