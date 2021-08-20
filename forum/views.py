from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm

def home(request):
    return render(request, "forum/home.html")

class PostFormView(FormView):
    template_name = 'forum/post.html'
    form_class = PostForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

# Create your views here.
