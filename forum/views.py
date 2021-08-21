from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import PostForm
from .models import Post

from slugify import slugify

def home(request):
    return render(request, "forum/home.html")

class PostDetailView(DetailView):
    template_name = 'forum/single_post.html'
    model = Post
    context_object_name = 'post'

class PostListView(ListView):
    template_name = 'forum/home.html'
    model = Post
    paginate_by = 10
    context_object_name = 'posts'


class PostFormView(FormView):
    template_name = 'forum/post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            try:
                title = form.cleaned_data['title']
                message = form.cleaned_data['message']
                excerpt = message[0:200] + "..."
                slug = slugify(title)
                user = self.request.user

                post = Post(title=title, message=message, excerpt=excerpt, slug=slug, user=user)

                post.save()

                return render(self.request, "forum/home.html")

            except:
                print("Couldn't save into Post model")

        return render(self.request, "forum/post.html", {
            "form": form
        })
# Create your views here.
