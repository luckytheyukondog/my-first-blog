from .models import Post, thick
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, ThicknessForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from calculator import calc

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def thickness_calc(request):
    result = None
    if request.method == "POST":
        form = ThicknessForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            angle = form.angle
            dhthick = form.dhthick
            result = calc(angle,dhthick)
            return render(request, 'blog/truewidthans.html', {'form':form, 'result': result})
    else:
        form = ThicknessForm()
    return render(request, 'blog/truewidth.html', {'form': form})
            
            
            
