from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post, Author, Comment, Tag


def index(request):
    """Главное страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return render(request, 'blog_app/about.html')


def post_list(request):
    """Список постов."""
    posts = Post.objects.all()
    context = {
        'title': 'Список постов',
        'posts': posts,
    }
    return render(request, 'blog_app/post_list.html', context=context)


def post_detail(request, post_id):
    """Детальный пост."""
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    # comments = Comment.objects.all()
    comments = post.comments.all()
    tags = post.tags.all()
    context = {
        # 'title': post.title,
        'post': post,
        'comments': comments,
        'tags': tags,
    }
    return render(request, 'blog_app/post_detail.html', context=context)


def post_add(request):
    """Представление для добавления нового поста через форму."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                rating=form.cleaned_data['rating'],
                author=Author.objects.first()
            )
            return redirect("post_list")
    else:
        form = PostForm()

    context = {
        'form': form,
        'title': "Добавить пост"
    }
    return render(request, 'blog_app/post_add.html', context=context)


def author_list(request):
    """Список авторов."""
    authors = Author.objects.all()
    context = {
        'title': 'Список Авторов',
        'authors': authors,
    }
    return render(request, 'blog_app/author_list.html', context=context)


def author_detail(request, author_id):
    """Посты автора."""
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author,
    }
    return render(request, 'blog_app/author_detail.html', context=context)