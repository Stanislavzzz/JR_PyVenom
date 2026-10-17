from django.urls import path

from .views import index, about, post_list


urlpatterns = [
    path('', index),
    path('about/', about),
    path('posts/', post_list),
]
