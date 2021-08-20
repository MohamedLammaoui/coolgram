from django import forms    
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.views.generic.edit import FormView

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Username',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
