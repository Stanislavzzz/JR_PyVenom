from django.core.management.base import BaseCommand
import random
from faker import Faker

from blog_app.models import Post, Author, Comment, Tag, AuthorProfile


class Command(BaseCommand):
    help = "Очистка данных"

    def handle(self, *args, **kwargs):
        """Выполняет удаление всех данных"""

        self.stdout.write("Начало удаления данных")

        Tag.objects.all().delete()
        AuthorProfile.objects.all().delete()
        Author.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()

        self.stdout.write("Удалили все данные")