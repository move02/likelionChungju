from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.
def show(request):
    posts = Post.objects

    post_list = Post.objects.all()
    paginator = Paginator(post_list,5)

    page = request.GET.get('page')
    post_s = paginator.get_page(page)

    return render(request,'show.html',{
    'posts':posts,
    'post_s':post_s
    })

def read(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm()
    return render(request,'read.html',{
    'post':post,
    'comment_form':comment_form
    })

def create(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/notice/show')
        else:
            return redirect('/create')

    else:
         form = PostForm()       
    
    return render(request,'create.html',{
        'post_form':form,
        })

def edit(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request,'read.html',{
                'post':post
            })

    else:
        form = PostForm(instance = post)
    return render(request,'edit.html',{
    'post_form':form,
    'post':post
    }
    )

def destroy(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    post.delete()

    return redirect('/notice/show')   

def comment_create(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/notice/read/'+str(post.id))

def comment_destroy(request,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    comment.delete()
    return redirect('/notice/read/'+str(comment.post.id))


    
    
