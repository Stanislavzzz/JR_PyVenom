from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import PostModelForm, PostDeleteForm, ContactForm
from .models import Post, Author, Comment, Tag


class IndexTemplateView(TemplateView):
    """Представление для отображения главной страницы."""
    template_name = 'blog_app/index.html'

# def index(request):
#     """Главное страница."""
#     return render(request, 'blog_app/index.html')


class AboutTemplateView(TemplateView):
    """Представления для отображения страницы "О нас"."""
    template_name = 'blog_app/about.html'

#
# def about(request):
#     """Страница о нас."""
#     return render(request, 'blog_app/about.html')


class ContactFormView(FormView):
    """Представление для обработки формы обратной связи."""
    template_name = 'blog_app/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        text = f'Спасибо за ваше обращение'
        messages.success(self.request, text)
        return super().form_valid(form)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постов'
        return context


class PostDetailView(PostBase, DetailView):
    """Представление для отображения одного поста."""
    # model = Post
    # context_object_name = 'post'
    # template_name = 'blog_app/post_detail.html'
    # ordering = ['-created_at']

    def get(self, request, *args, **kwargs):
        """Перепопределяем метод get."""
        post = self.get_object()
        post.views = getattr(post, 'views', 0) + 1
        post.save(update_fields=['views'])
        return super().get( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.all()
        tags = self.object.tags.all()
        context['comments'] = comments
        context['tags'] = tags
        return context


class PostCreateView(PostBase, CreateView):
    """Представление для добавления нового поста через форму."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        """Добавляем сообщение об успешном создании поста."""
        title = form.cleaned_data['title']
        text = f"Ваш пост: '{title}' успешно создан"
        messages.success(self.request, text)
        return super().form_valid(form)


class PostUpdateView(PostBase, UpdateView):
    """Представление для обновления поста через форму."""
    # model = Post
    # template_name = 'blog_app/post_form.html'
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


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



