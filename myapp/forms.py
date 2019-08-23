from django import forms
from .models import *
from django.contrib.auth.models import *

class Regform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']

        
class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['location','job_title','pic']


class postform(forms. ModelForm):
    
    title=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Title'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Comment','row':4,'cols':30,'style':'resize:none;'}))

    class Meta:
        model=Post
        fields=['title','content']
        
