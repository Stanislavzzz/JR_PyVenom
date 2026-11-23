import pytest
from django.urls import reverse
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_post_list_templates(client, post_1, post_2, post_3):
    """Проверка шаблона post_list.html."""
    url = reverse('post_list')
    response = client.get(url)

    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    h5_list = soup.find_all('h5')
    titles = [h5.get_text() for h5 in h5_list]
    # assert len(titles) == 4
    assert post_1.title in titles
    assert post_2.title in titles
    assert post_3.title in titles