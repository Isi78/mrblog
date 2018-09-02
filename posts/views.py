from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment


'''
def lista_post(request):
    return render(request, 'lista_post.html')
    

def post_singolo(request):
    return render(request, 'post_singolo.html')
'''

def contatti(request):
    return render(request, 'contatti.html')


def commenti(request):
    return render(request, 'commenti.html')

def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            post.comment = comment
            comment.save()
            return redirect('/', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
# Create your views here.
