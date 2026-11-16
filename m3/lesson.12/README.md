# Создание виртуального окружения
python -m venv .venv
source ./.venv/bin/activate
.\.venv\Scripts\activate.ps1
deactivate

# Установка Django
pip install django 

# Проверяем версию django
django-admin --version

# Создание проекта django во вложенной директории
django-admin startproject blog

# Создание проекта django в текущей директории config
django-admin startproject config .

# Запустить проект
python manage.py runserver

# Создание приложения blog_app
python manage.py startapp blog_app

# Создать миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Интерактивная консоль Django
python manage.py shell

# CRUD операции 
# Create
post = Post(title='Первый пост', content='Привет, мир!', author='Bob')
post.save()

# READ - получить все объекты
all_post = Post.objects.all()

# вывести первый объект из all_post
first_post = all_post[0]
first_post.title

# Create OneToMany
post1 = Post.objects.create(title='Важный пост', content='Завтра новая версия python', author='Admin')   
comment1 = Comment.objects.create(text='Отличная новость', author='User123', post=post1)   
comment2 = Comment.objects.create(text='Отличная новость2', author='User345',
post=post1)   

# READ - получить связанный объект
comment1.post.title   
> 'Важный пост'   
   
# READ - получить связанные объект
post1.comments.all()    
> <QuerySet [<Comment: Коммент автора User123>, <Comment: Коммент автора User345>]>   


# Django ORM 2


###  OneToOne

Создать автора

`author = Author.objects.create(name="Anna")`

Создать профиль автора (OneToOne)

`profile = AuthorProfile.objects.create(author=author, bio="Программист Python", website="https://google.ru")`

Получить биографию через автора

`author.profile.bio`

Получить имя автора через профиль

`profile.author.name`

### ManyToMany

Создать первый пост

`post = Post.objects.create(title="Python пост", content="Вышла новая версия Python 3.15", author="Admin")`

Создать второй пост

`post2 = Post.objects.create(title="Web пост", content="Вышла новая версия Django 6.1", author="Bob")`

Создать теги

`tag1 = Tag.objects.create(name="Django")` `tag2 = Tag.objects.create(name="Python")` `tag3 = Tag.objects.create(name="Web")`

Добавить теги к постам (ManyToMany)

`post.tags.add(tag1, tag2)` `post2.tags.add(tag2, tag3)`

Получить все теги поста

`post.tags.all()`

Получить все посты с определённым тегом

`tag2.posts.all()`

### Fixtures - импорт и экспорт данных

Загрузить данные из JSON-файла в базу данных

`python manage.py loaddata ./blog_fixtures.json`

Вывести все данные приложения blog_app в JSON

`python manage.py dumpdata blog_app`

Экспортировать все данные приложения в JSON-файл

`python manage.py dumpdata blog_app > ./fixtures/blog_app_all_export.json`

Экспортировать данные в JSON с отступами

`python manage.py dumpdata blog_app --indent 4 > ./fixtures/blog_app_all_new_export.json`

Экспортировать только объекты модели Post

`python manage.py dumpdata blog_app.Post > ./fixtures/post_all_export.json`

Экспортировать объекты Post с отступами

`python manage.py dumpdata blog_app.Post --indent 4 > ./fixtures/post_all_export.json`

Экспортировать несколько моделей (Tag и Author)

`python manage.py dumpdata blog_app.Tag blog_app.Author --indent 4 > ./fixtures/selected_all_export.json`

Установить библиотеку для работы с YAML

`pip install pyyaml`

Экспортировать объекты Post в формате YAML

`python manage.py dumpdata blog_app.Post --format yaml > ./fixtures/post_yaml_export.yaml`

Загрузить данные из YAML-файла

`python manage.py loaddata ./fixtures/post_yaml_export.yaml`

### Получение и фильтрация объектов

READ - получить автора по имени

`author = Author.objects.get(name="John")`

READ - получить все посты автора

`author.posts.all()`

READ - получить все посты с тегом Python

`Tag.objects.get(name="Python").posts.all()`

READ - получить все посты

`all_posts = Post.objects.all()`

FILTER - найти посты, содержащие Django в заголовке

`django_posts = all_posts.filter(title__contains="Django")`

FILTER - найти посты, содержащие Python в заголовке

`python_posts = Post.objects.filter(title__contains="Python")`

READ - получить первый пост из отфильтрованных

`python_post_1 = python_posts[0]`

READ - получить рейтинг поста

`python_post_1.rating`

### Изменение и удаление объектов

UPDATE - изменить рейтинг поста

`python_post_1.rating = 10` `python_post_1.save()`

READ - проверить изменённый рейтинг

`python_post_1.rating`

DELETE - найти автора по имени

`author_eve = Author.objects.get(name="Eve")`

DELETE - удалить автора

`author_eve.delete()`

### Сортировка объектов

ORDER BY - сортировка авторов по имени (А-Я)

`Author.objects.all().order_by("name")`

ORDER BY - сортировка авторов по имени в обратном порядке (Я-А)

`Author.objects.all().order_by("-name")`

ORDER BY - сортировка постов по рейтингу по возрастанию

`Post.objects.all().order_by("rating")`

ORDER BY - сортировка постов по рейтингу по убыванию

`Post.objects.all().order_by("-rating")`



=========

<!--{% load static %}-->

<!--    <link rel="stylesheet" href="{% static 'blog_app/css/site.css %}">-->

<!--    <script src="{% static 'blog_app/js/site.js %}"></script>-->