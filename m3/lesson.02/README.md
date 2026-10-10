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