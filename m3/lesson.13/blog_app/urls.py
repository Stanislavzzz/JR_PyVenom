from django.urls import path
from django.views.generic.base import RedirectView

from .views import author_detail, author_list, IndexTemplateView, AboutTemplateView, ContactFormView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('old-about/', RedirectView.as_view(url='/about/'), name='old-about'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/add/', PostCreateView.as_view(), name='post_add'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    # path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('authors/', author_list, name='author_list'),
    path('authors/<int:author_id>/', author_detail, name='author_detail'),
]
