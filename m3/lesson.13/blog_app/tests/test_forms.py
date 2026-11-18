import pytest

from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author


@pytest.mark.django_db
def test_post_form_valid():
    """Проверка валидации PostForm."""
    form_data = {
        'title': 'Тестовый пост формы',
        'content': 'Это содержание формы тестового поста',
        'rating': 10,
    }
    form = PostForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_post_form_invalid_rating():
    """Проверка не валидности PostForm поля rating."""
    form_data = {
        'title': 'Тестовый пост формы',
        'content': 'Это содержание формы тестового поста',
        'rating': 101,
    }
    form = PostForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_post_modelform_valid(author_1):
    """Проверка валидации PostModelForm."""
    form_data = {
        'title': 'Тестовый пост PostModelForm',
        'content': 'Это содержание PostModelForm тестового поста',
        'rating': 7,
        'author': author_1,
    }
    form = PostModelForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_invalid(author_1):
    """Проверка валидации поля PostModelForm на запрещенные слова."""
    form_data = {
        'title': 'Тестовый пост PostModelForm',
        'content': 'Это содержание крипта PostModelForm тестового поста',
        'rating': 7,
        'author': author_1,
    }
    form = PostModelForm(data=form_data)
    assert not form.is_valid()