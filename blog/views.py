from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogPostForm, RegisterForm
from .models import BlogPost


def home(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    posts = BlogPost.objects.filter(is_published=True).select_related("author")

    if query:
        posts = posts.filter(title__icontains=query) | posts.filter(
            content__icontains=query
        )

    if category:
        posts = posts.filter(category=category)

    posts = posts.distinct()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = BlogPost.objects.filter(
        is_published=True
    ).values_list("category", flat=True).distinct()

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "query": query,
        "selected_category": category,
    }
    return render(request, "home.html", context)


def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if not post.is_published and post.author != request.user:
        return get_object_or_404(BlogPost, pk=pk, is_published=True)

    return render(request, "post_detail.html", {"post": post})


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Blog post created successfully.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = BlogPostForm()

    return render(request, "post_form.html", {
        "form": form,
        "page_title": "Create Post",
        "button_text": "Publish Post",
    })


@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)

    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = BlogPostForm(instance=post)

    return render(request, "post_form.html", {
        "form": form,
        "page_title": "Edit Post",
        "button_text": "Update Post",
    })


@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Blog post deleted successfully.")
        return redirect("my_posts")

    return render(request, "post_confirm_delete.html", {"post": post})


@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    paginator = Paginator(posts, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "my_posts.html", {"page_obj": page_obj})
