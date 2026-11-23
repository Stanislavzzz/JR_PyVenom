import pytest

from blog_app.models import Post, Author


@pytest.fixture
def author_1():
    """Фикстура для создания 1 автора."""
    return Author.objects.create(name='Bob')


@pytest.fixture
def author_2():
    """Фикстура для создания 2 автора."""
    return Author.objects.create(name='Mary')


@pytest.fixture
def post_1(author_1: Author):
    """Фикстура для создания 1 поста."""
    return Post.objects.create(
        title='Тестовый Post 1',
        content='Text 1 поста 1',
        author=author_1,
        rating=3
    )


@pytest.fixture
def post_2(author_1: Author):
    """Фикстура для создания 2 поста."""
    return Post.objects.create(
        title='Тестовый Post 2',
        content='Text 2 поста 2',
        author=author_1,
        rating=5
    )


@pytest.fixture
def post_3(author_2: Author):
    """Фикстура для создания 3 поста."""
    return Post.objects.create(
        title='Тестовый Post 3',
        content='Text 3 поста 3',
        author=author_2,
        rating=7
    )
