from django.shortcuts import render
from .forms import *
from django.http import *
from django.contrib.auth.models import *
# Create your views here.
from .models import *
from django.contrib import auth


def login(request):
    
    if request.method=='POST':

        user = request.POST['username']
        pwd = request.POST['password']
        print(user,pwd)
        user = auth.authenticate(username=user,password=pwd)
        print(user)
        if user is not None:
            auth.login(request,user)
            
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('invalid')
        
    
    return render(request,'login.html')



def index(request):
    if request.method=='POST':
        form=postform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
                #obj=post(title=form.cleaned_data['title'],content=form.cleaned_data['content'])
            instance=form.save(commit=False) #obj
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form=postform()
        #data=Post.objects.all()
        data=Post.objects.order_by('-id')
    return render(request,'index1.html',{'form':form,'data':data})

def sign_up(request):
    if request.method=='POST':
        regform=Regform(request.POST)
        profile_form=Profileform(request.POST,request.FILES)
        if  regform.is_valid() and profile_form.is_valid():
            username = regform.cleaned_data.get('username')
            email = regform.cleaned_data.get('email')
            password = regform.cleaned_data.get('password')
            
            User.objects.create_user(username=username, password=password,
                                     email=email)
            #regform.save()
            u=User.objects.get(username=username)
            f=profile_form.save(commit=False)
            f.user=u
            f.save()
            return HttpResponseRedirect('/')
            
    else:
        regform=Regform()
        profile_form=Profileform()
    return render(request,'home.html',{'regform':regform,
                                        'profile_form':profile_form})  


def home(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return login(request)


def delete(request,d):
    n=Post.objects.get(id=d)
    n.delete()
    return HttpResponseRedirect('/')

def logout(request):
    auth.logout(request)
    #return render(request,'login.html')
    return HttpResponseRedirect('/')
