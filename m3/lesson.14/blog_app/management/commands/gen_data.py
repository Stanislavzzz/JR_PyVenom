from django.core.management.base import BaseCommand
import random
from faker import Faker

from blog_app.models import Post, Author, Comment, Tag, AuthorProfile


class Command(BaseCommand):
    help = "Генерация случайных данных"

    def handle(self, *args, **kwargs):
        """Выполняет создание тестовых данных"""

        self.stdout.write("Начало генерации данных")

        faker = Faker("ru_RU")

        # Генерация авторов
        authors = []

        for _ in range(random.randint(5, 10)):
            author = Author.objects.create(
                name = faker.first_name(),
            )

            AuthorProfile.objects.create(
                author = author,
                bio = faker.text(max_nb_chars=random.randint(50, 100)),
                website = faker.url(),
            )
            authors.append(author)

        self.stdout.write(f"Завершили создание авторов - {len(authors)}")

        # Генерация тегов
        tags = []

        for _ in range(random.randint(10, 20)):
            tag = Tag.objects.create(
                name = faker.word(),
            )

            tags.append(tag)
        self.stdout.write(f"Завершили создание тегов - {len(tags)}")

        # Генерация постов
        posts = []

        for _ in range(random.randint(10, 15)):

            tag_post = random.sample(tags, random.randint(1, 5))

            post = Post.objects.create(
                title = faker.sentence(nb_words=random.randint(3, 10)),
                author = random.choice(authors),
                content = faker.text(max_nb_chars=random.randint(300, 700)),
                rating = random.randint(1, 10),
            )

            post.tags.add(*tag_post)
            posts.append(post)

        self.stdout.write(f"Завершили создание постов - {len(posts)}")

        # Генерация постов
        comments = []

        for _ in range(random.randint(30, 50)):
            comment = Comment.objects.create(
                author = random.choice(authors),
                text = faker.text(max_nb_chars=random.randint(50, 500)),
                post = random.choice(posts),
            )
            comments.append(comment)

        self.stdout.write(f"Завершили создание комментариев - {len(comments)}")


        self.stdout.write("Завершение генерации данных")