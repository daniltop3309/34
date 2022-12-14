from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from .models import PostList


def former(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    posts = PostList.objects.all()
    return render(request, 'index1.html', {'plist': posts})


def delete(request, id):
    try:
        post = PostList.objects.get(pk = id)
        post.delete()
        return redirect('index')
    except PostList.DoesNotExist:
        return HttpResponseNotFound('<h2>post not found</h2>')

def edit(request, id):
    try:
        post = PostList.objects.get(pk = id)
        if request.method == 'POST':
            post.name = request.POST.get('name')
            post.age = request.POST.get('age')
            post.save()
            return redirect('index')
        else:
            return render(request, 'edit.html', {'post':post})
    except PostList.DoesNotExist:
        return HttpResponseNotFound('<h2>post not found</h2>')
