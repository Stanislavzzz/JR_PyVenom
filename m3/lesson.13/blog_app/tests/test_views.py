import pytest
from django.urls import reverse


def test_index_view(client):
    """Тест для проверки корректности работы главной страницы блога."""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Добро пожаловать!' in response.content.decode()