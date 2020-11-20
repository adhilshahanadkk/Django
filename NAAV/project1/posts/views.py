from django.shortcuts import render
from posts.models import Post
from posts.forms import PostForms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(is_active=True)
    return render(request, 'post/post_list.html',{"posts":posts})
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post/post_detail.html', {'post': post})
def new_post(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author =request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForms()
        return render(request, 'post/new_post.html',{'form':form})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def contact(request):
    return render(request, 'post/contactus.html')

def service(request):
    return render(request, 'post/service.html')

def base(request):
    return render(request, 'post/base.html')
def map1(request):
    return render(request, 'post/map1.html')
def map2(request):
    return render(request, 'post/map2.html')
def about(request):
    return render(request, 'post/about.html')