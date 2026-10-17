from django.shortcuts import render

from .models import Post


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
