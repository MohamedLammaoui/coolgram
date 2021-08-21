from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm

def home(request):
    return render(request, "forum/home.html")

class PostFormView(FormView):
    template_name = 'forum/post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
       title = form.cleaned_data['title']
       message = form.cleaned_data['message']
       print('it went here')
       print(f'{title} with the following message: {message}')
       

# Create your views here.
