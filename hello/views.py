from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.http import Http404
from .form import PostForm
from django.utils import timezone

def index(request):
    try:
        list = Post.objects.order_by('-pub_date')[:]
    except Post.DoesNotExist:
        raise Http404("Post Not Found")

    context = {'list': list}
    return render(request, 'hello/index.html', context)

def detail(request, question_id):
    context = {'id': question_id}
    return render(request, 'hello/index.html', context)

def comment(request, question_id):
    return HttpResponse("You're commenting on post %s." % question_id)

def create(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'hello/form.html', {'form': form})
