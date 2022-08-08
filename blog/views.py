from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def home(request):

    post_list = Post.objects.all().order_by("-created")

    paginator = Paginator(post_list, 5)

    page = request.GET.get("page", 1)

    page_obj = paginator.get_page(page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts, "page_obj": page_obj}

    return render(request, "blog/index.html", context)


def createPost(request):

    if request.method == "POST":

        if request.POST.get("content") == "":
            messages.error(request, "Post cannot be empty")
        else:
            body = request.POST.get("content")
            new_post = Post.objects.create(body=body)
            new_post.save()
            return redirect("home")

    return redirect("home")


def about(request):
    return render(request, "blog/about.html")


def post(request, pk):

    post = Post.objects.get(id=pk)

    if post is None:
        messages.error(request, "Post doesnt exists")

    context = {"post": post}
    return render(request, "blog/single_post.html", context)
