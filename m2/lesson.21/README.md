# Работа с Docker Compose

## 📁 Файлы проекта

```text
project/
├── compose.yaml
├── Dockerfile
├── db_check.py
├── pyproject.toml
├── poetry.lock
├── .env
└── .dockerignore
```

---

## 🐳 Ручной запуск без Compose

### Собрать образ приложения

```bash
docker build -t compose-app:1.0 .
```

* `-t compose-app:1.0` — имя и тег образа;
* `.` — текущая папка с Dockerfile.

### Создать Docker-сеть

```bash
docker network create app-network1
```

### Запустить PostgreSQL

```bash
docker run -d \
  --name postgres \
  --network app-network1 \
  -e POSTGRES_DB=app_db \
  -e POSTGRES_USER=app_user \
  -e POSTGRES_PASSWORD=app_password \
  postgres:17-alpine
```

### Запустить Python-приложение

```bash
docker run --rm \
  --name app \
  --network app-network1 \
  --env-file .env \
  compose-app:1.0
```

Главное:

```text
app → postgres:5432
```

Оба контейнера находятся в `app-network1`.

---

# 📝 Основы YAML

YAML использует:

```text
ключ: значение
```

Пример:

```yaml
name: Alex
age: 25
```

Аналог Python-словаря:

```python
user = {
    "name": "Bob",
    "age": 25,
}
```

---

## 📋 Списки

Python:

```python
port = [
    "8000:8000",
    "8000:8001",
]
```

YAML:

```yaml
port:
  - "8000:8000"
  - "8000:8001"
```

`-` обозначает элемент списка.

---

## 📂 Вложенность

```yaml
services:
  db:
    image: postgres
```

Структура определяется **отступами**:

```text
services
└── db
    └── image
```

Обычно используем 2 пробела.

---

# 📄 Имена Compose-файла

Можно встретить:

```text
compose.yaml
compose.yml
docker-compose.yaml
docker-compose.yml
```

В новых проектах используем:

```text
compose.yaml
```

---

# 🔄 Старый и новый синтаксис Compose

Старый:

```bash
docker-compose build
```

Современный:

```bash
docker compose build
```

Для курса используем:

```bash
docker compose ...
```

---

# 🧩 Текущий `compose.yaml`

```yaml
services:
  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password

  app:
    build: .
    command: ["python", "db_check.py"]

    environment:
      DB_HOST: ${DB_HOST}
      DB_PORT: ${DB_PORT}
      DB_NAME: ${DB_NAME}
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
```

---

## Основные конструкции

### `services`

```yaml
services:
```

Сервисы нашего проекта.

Сейчас:

```text
db  → PostgreSQL
app → Python-приложение
```

### `image`

```yaml
image: postgres:17-alpine
```

Использовать готовый Docker-образ.

### `build`

```yaml
build: .
```

Собрать образ нашего приложения из Dockerfile текущей папки.

Кратко:

```text
image → готовый образ
build → собрать свой образ
```

### `command`

```yaml
command: ["python", "db_check.py"]
```

Команда, которая запускается внутри контейнера `app`.

### `environment`

```yaml
environment:
  POSTGRES_DB: app_db
```

Переменные окружения контейнера.

---

# ⚙️ `.env`

Текущий файл:

```env
DB_HOST=postgres
DB_PORT=5432
DB_NAME=app_db
DB_USER=app_user
DB_PASSWORD=app_password
```

Python получает значения через:

```python
os.getenv("DB_HOST")
```

### Важно

Для **ручного запуска**, где контейнер называется:

```bash
--name postgres
```

правильно:

```env
DB_HOST=postgres
```

Когда `app` будем запускать именно через Compose и обращаться к сервису:

```yaml
db:
```

адресом станет:

```env
DB_HOST=db
```

---

# 🐍 `db_check.py`

```python
import os
import psycopg

# Настройки подключения
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "app_db")
DB_USER = os.getenv("DB_USER", "app_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "app_password")

try:
    # Подключаемся к PostgreSQL
    with psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    ) as connection:

        # Проверяем соединение простым запросом
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

        print("Подключение к PostgreSQL успешно")
        print(f"Ответ базы: {result}")

except Exception as error:
    print("Ошибка подключения к PostgreSQL")
    print(error)
```

Установка драйвера:

```bash
poetry add "psycopg[binary]"
```

---

# 🐳 Dockerfile приложения

Текущий Dockerfile:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

CMD ["python", "db_check.py"]
```

Здесь:

```text
FROM    → базовый образ
WORKDIR → рабочая папка
ENV     → переменные окружения
RUN     → выполнить команду при сборке
COPY    → скопировать файлы
CMD     → команда запуска контейнера
```

---

# 🏗️ Команды Compose, которые прошли

### Собрать все сервисы с `build`

```bash
docker compose build
```

### Собрать только `app`

```bash
docker compose build app
```

Compose видит:

```yaml
app:
  build: .
```

и собирает приложение через Dockerfile.

### Запустить только PostgreSQL

```bash
docker compose up -d db
```

* `up` — создать и запустить;
* `-d` — в фоне;
* `db` — только сервис `db`.

---

# 📌 Главное

```text
Dockerfile
→ как собрать образ приложения

compose.yaml
→ как описать несколько сервисов
```

```text
db
→ готовый postgres image

app
→ собирается через Dockerfile
```

```text
docker-compose
→ старый синтаксис

docker compose
→ современный синтаксис
```

На текущем этапе основные команды:

```bash
docker build -t compose-app:1.0 .

docker network create app-network1

docker run -d --name postgres --network app-network1 \
  -e POSTGRES_DB=app_db \
  -e POSTGRES_USER=app_user \
  -e POSTGRES_PASSWORD=app_password \
  postgres:17-alpine

docker run --rm --name app \
  --network app-network1 \
  --env-file .env \
  compose-app:1.0

docker compose build

docker compose up -d db

docker compose build app
```

