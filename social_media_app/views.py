  
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm,PostForm

def showsignuppage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)

			return redirect('login')
			

	context = {'form':form}
	return render(request, 'signup2.html', context)
# Create your views here.

@login_required(login_url='login')
def home(request):
    pic = Like.objects.all()
    arr=[]
    pid=[]
    arr = pic.filter(user=request.user)
    for i in range(len(arr)):
        pid.append(arr[i].picture.id)
    print(pid)
    context = {
        'posts': Post.objects.all(),
        'pid':pid
    }
    return render(request,'index.html',context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    return render(request, 'login.html')

def logoutpage(request):
    return redirect('login')

@login_required(login_url='login')
def myPost(request):
    pic = Like.objects.all()
    arr=[]
    pid=[]
    arr = pic.filter(user=request.user)
    for i in range(len(arr)):
        pid.append(arr[i].picture.id)
    print(pid)
    context = {
        'posts': Post.objects.all(),
        'pid': pid,
    }

    return render(request,'profile.html',context)

@login_required(login_url='login')
def newPost(request):
    initial_data={            #1st Method
        'author': request.user.id,
        'title':"Title",
        'image':"",
        'content':"Content",
    }
    form = PostForm(initial=initial_data)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # data=int(form["author"].value())
        # if data == request.user.id: 
        if form.is_valid():
            form.save()
            return redirect('myPost')
        else:
            print("no ")
			

    context = {'form':form}
    return render(request,'makepost.html',context)

@login_required(login_url='login')
def postpage(request):
    return render(request,'post.html')

@login_required(login_url='login')
def delete_post(request,post_id):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('myPost')

@login_required(login_url='login')
def edit_post(request,post_id):
    post_to_edit=Post.objects.get(id=post_id)
    form=PostForm(instance=post_to_edit)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        data=int(form["author"].value())
        if data == request.user.id: 
            if form.is_valid():
                form.save()
                post_to_edit.delete()
                return redirect('myPost')
        else:
            print("no ")
			

    context = {'form':form}
    return render(request,'makepost.html',context)


@login_required(login_url='login')
def like_post(request,post_id):
    pic = Post.objects.get(id=post_id)
    user_likes_this = pic.like_set.filter(user=request.user)
    if user_likes_this:
        print("already liked")
        Like.objects.filter(user=request.user,picture=post_id).delete()
    else:
        new_like, created = Like.objects.get_or_create(user=request.user, picture_id=post_id)
    context = {
        'posts': Post.objects.all(),
    }
    return redirect('home')