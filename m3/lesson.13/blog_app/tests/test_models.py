import pytest

from blog_app.models import Post, Author


@pytest.mark.django_db
def test_create_author(author_1: Author, author_2: Author):
    """Тест создания автора."""
    assert Author.objects.count() == 2
    assert author_1.name == 'Bob'
    assert author_2.name == 'Mary'
    assert str(author_1) == 'Bob !'


@pytest.mark.django_db
def test_create_posts(post_1: Post, post_2: Post, post_3: Post):
    """Тест создания постов."""
    assert Post.objects.count() == 3
    assert post_1.title == 'Тестовый Post 1'
    assert post_2.rating == 5
    assert str(post_3) == "Пост Тестовый Post 3!"