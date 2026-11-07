from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostModelForm, PostDeleteForm
from .models import Post, Author, Comment, Tag


def index(request):
    """Главное страница."""
    return render(request, 'blog_app/index.html')


def about(request):
    """Страница о нас."""
    return render(request, 'blog_app/about.html')


class PostBase:
    model = Post


class PostListView(PostBase, ListView):
    """Представление для отображения списка постов."""
    # model = Post
    context_object_name = 'posts'
    # template_name = 'blog_app/post_list.html'
    # ordering = ['-created_at']

    def get_queryset(self):
        # return super().get_queryset().filter(is_published=True)
        queryset =  super().get_queryset()
        author_id =  self.request.GET.get('name')
        min_rating = self.request.GET.get('rating')

        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        return queryset


# def post_list(request):
#     """Список постов."""
#     posts = Post.objects.all()
#     context = {
#         'title': 'Список постов',
#         'posts': posts,
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


class PostDetailView(PostBase, DetailView):
    """Представление для отображения одного поста."""
    pass
    # model = Post
    # context_object_name = 'post'
    # template_name = 'blog_app/post_detail.html'

    # ordering = ['-created_at']


# def post_detail(request, post_id):
#     """Детальный пост."""
#     post = get_object_or_404(Post, pk=post_id)
#     comments = post.comments.all()
#     tags = post.tags.all()
#     context = {
#         'post': post,
#         'comments': comments,
#         'tags': tags,
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


class PostCreateView(PostBase, CreateView):
    """Представление для добавления нового поста через форму."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


# def post_add(request):
#     """Представление для добавления нового поста через форму."""
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post_list")
#     else:
#         form = PostModelForm()
#
#     context = {
#         'form': form,
#         'title': "Добавить пост"
#     }
#     return render(request, 'blog_app/post_add.html', context=context)


class PostUpdateView(PostBase, UpdateView):
    """Представление для обновления поста через форму."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


# def post_edit(request, post_id):
#     """Представление для редактирования существующего поста."""
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect("post_list")
#     else:
#         form = PostModelForm(instance=post)
#
#     context = {
#         'form': form,
#         'title': "Изменить пост"
#     }
#     return render(request, 'blog_app/post_edit.html', context=context)


# def post_delete(request, pk):
#     """Представление для удаления существующего поста."""
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         form = PostDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirm']:
#             post.delete()
#             return redirect("post_list")
#     else:
#         form = PostDeleteForm()
#
#     context = {
#         'form': form,
#         'title': "Удалить пост",
#         'post': post
#     }
#     return render(request, 'blog_app/post_delete.html', context=context)


class PostDeleteView(PostBase, DeleteView):
    """Представление для удаления поста."""
    # model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')
    form_class = PostDeleteForm


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