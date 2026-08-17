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


# ⚙️ `env_file`

Для приложения можно передать переменные из файла:

```yaml
app:
  build: .
  command: ["python", "db_check.py"]
  env_file:
    - .env
```

Файл `.env`:

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=app_db
DB_USER=app_user
DB_PASSWORD=app_password
```

```text
env_file
→ передаёт переменные из файла внутрь контейнера
```

В Python:

```python
os.getenv("DB_HOST")
```

получит:

```text
db
```

---

# 🌐 Сеть Docker Compose

Compose автоматически создаёт общую сеть проекта.

Поэтому отдельно выполнять:

```bash
docker network create ...
```

обычно не требуется.

Сервисы обращаются друг к другу **по имени сервиса**:

```text
app → db:5432
```

Если PostgreSQL описан:

```yaml
services:
  db:
```

то:

```env
DB_HOST=db
```

Важно:

```text
localhost внутри app
→ сам контейнер app

db
→ контейнер PostgreSQL
```

---

## Явная сеть

При необходимости сеть можно описать самостоятельно:

```yaml
services:
  db:
    networks:
      - app-network

  app:
    networks:
      - app-network

networks:
  app-network:
```

Для простого проекта это необязательно.

---

# 🔌 `ports`

Аналог обычного Docker:

```bash
docker run -p 8000:8000 ...
```

В Compose:

```yaml
ports:
  - "8000:8000"
```

Формат:

```text
HOST_PORT:CONTAINER_PORT
```

Например:

```yaml
ports:
  - "8080:8000"
```

```text
localhost:8080 → container:8000
```

Для связи контейнеров:

```text
app → db:5432
```

`ports` не нужен.

Публикуем порт только если сервис должен быть доступен **с хостовой машины**.

---

# 💾 Named volume в Compose

Подключаем volume к PostgreSQL:

```yaml
services:
  db:
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```text
volumes внутри db
→ подключить хранилище

volumes верхнего уровня
→ объявить named volume
```

Compose сам создаёт volume.

Проверить:

```bash
docker volume ls
```

Named volume продолжает существовать после удаления контейнера.

---

## Bind mount и named volume

Named volume:

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

```text
→ управляется Docker
→ удобно для PostgreSQL и постоянных данных
```

Bind mount:

```yaml
volumes:
  - ./data:/app/data
```

```text
→ конкретная папка хоста
→ удобно для кода, конфигов и файлов проекта
```

Для bind mount отдельный верхнеуровневый:

```yaml
volumes:
```

не требуется.

---

# 🔗 `depends_on`

Простая зависимость:

```yaml
app:
  depends_on:
    - db
```

Означает:

```text
сначала запустить db
↓
потом app
```

Но важно:

```text
container started
≠
service ready
```

То есть контейнер PostgreSQL уже может быть запущен, но сама база ещё не готова принимать подключения.

---

# ❤️ `healthcheck`

Для PostgreSQL:

```yaml
healthcheck:
  test: ["CMD", "pg_isready", "-U", "app_user", "-d", "app_db"]
  interval: 5s
  timeout: 3s
  retries: 5
```

Основные параметры:

```text
test
→ команда проверки

interval
→ как часто выполнять

timeout
→ сколько ждать одну проверку

retries
→ сколько неудачных проверок допускается
```

Состояния:

```text
starting
healthy
unhealthy
```

Проверить:

```bash
docker compose ps
```

---

# 🔗 `depends_on` + `service_healthy`

Чтобы `app` дождался реальной готовности PostgreSQL:

```yaml
app:
  depends_on:
    db:
      condition: service_healthy
```

Теперь:

```text
db запускается
↓
healthcheck
↓
db становится healthy
↓
запускается app
```

---

# 🔄 Restart policy

Для долгоживущего сервиса, например PostgreSQL:

```yaml
db:
  restart: unless-stopped
```

```text
unless-stopped
→ автоматически перезапускать контейнер
→ кроме случая, когда его остановили вручную
```

Не путать с:

```bash
docker compose restart db
```

```text
restart: unless-stopped
→ автоматическая политика

docker compose restart
→ ручной перезапуск
```

---

# 🩺 Диагностика Compose

Базовый порядок:

```text
ps
↓
logs
↓
exec
```

## Проверить состояние

```bash
docker compose ps
```

Включая завершённые:

```bash
docker compose ps -a
```

---

## Посмотреть логи

Все сервисы:

```bash
docker compose logs
```

PostgreSQL:

```bash
docker compose logs db
```

Приложение:

```bash
docker compose logs app
```

Следить за логами:

```bash
docker compose logs -f db
```

`Ctrl + C` прекращает просмотр логов, но не останавливает контейнер.

---

## Выполнить команду внутри контейнера

```bash
docker compose exec db pg_isready
```

Более точная проверка:

```bash
docker compose exec db \
  pg_isready -U app_user -d app_db
```

Открыть shell:

```bash
docker compose exec db sh
```

Выйти:

```bash
exit
```

---

# ▶️ Одноразовый запуск `app`

Наш `db_check.py` выполняется и завершается, поэтому удобно:

```bash
docker compose run --rm app
```

```text
run
→ создать отдельный контейнер сервиса

--rm
→ удалить его после завершения
```

---

# 🏗️ Запуск и пересборка

Запустить проект:

```bash
docker compose up
```

В фоне:

```bash
docker compose up -d
```

С пересборкой:

```bash
docker compose up --build
```

В фоне с пересборкой:

```bash
docker compose up -d --build
```

Если изменили:

```text
Dockerfile
Python-код
pyproject.toml
poetry.lock
```

используем:

```bash
docker compose up -d --build
```

---

# ⏹️ Жизненный цикл Compose-проекта

## Остановить

```bash
docker compose stop
```

```text
контейнеры → остаются
сеть       → остаётся
volume     → остаётся
```

---

## Запустить остановленные контейнеры

```bash
docker compose start
```

`start` запускает уже существующие контейнеры.

---

## Перезапустить

```bash
docker compose restart
```

Один сервис:

```bash
docker compose restart db
```

---

## Удалить контейнеры и сеть

```bash
docker compose down
```

```text
контейнеры → удаляются
Compose-сеть → удаляется
named volume → остаётся
```

После `down` снова запускаем:

```bash
docker compose up -d
```

---

## Удалить ещё и volumes

```bash
docker compose down -v
```

```text
контейнеры → удаляются
сеть       → удаляется
volumes    → удаляются
данные     → удаляются
```

⚠️ Для PostgreSQL это означает удаление данных из named volume.

---

# 📊 Краткое сравнение

```text
stop
→ остановить контейнеры
→ контейнеры остаются

start
→ запустить существующие контейнеры

restart
→ перезапустить существующие контейнеры

down
→ удалить контейнеры и сеть
→ volumes оставить

down -v
→ удалить контейнеры, сеть и volumes
```

---

# 🧩 Текущий вариант `compose.yaml`

```yaml
services:
  db:
    image: postgres:17-alpine

    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password

    volumes:
      - postgres_data:/var/lib/postgresql/data

    healthcheck:
      test: ["CMD", "pg_isready", "-U", "app_user", "-d", "app_db"]
      interval: 5s
      timeout: 3s
      retries: 5

    restart: unless-stopped

  app:
    build: .
    command: ["python", "db_check.py"]

    env_file:
      - .env

    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres_data:
```

`.env`:

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=app_db
DB_USER=app_user
DB_PASSWORD=app_password
```

---

# 🧭 Основные команды

```bash
# Собрать app
docker compose build app

# Запустить проект
docker compose up -d

# Пересобрать и запустить
docker compose up -d --build

# Проверить состояние
docker compose ps
docker compose ps -a

# Логи
docker compose logs db
docker compose logs app
docker compose logs -f db

# Проверить PostgreSQL
docker compose exec db \
  pg_isready -U app_user -d app_db

# Одноразово запустить приложение
docker compose run --rm app

# Остановить
docker compose stop

# Запустить снова
docker compose start

# Перезапустить
docker compose restart

# Удалить контейнеры и сеть
docker compose down

# Удалить ещё и volumes
docker compose down -v
```

---

# 📌 Главное

```text
env_file
→ передать переменные контейнеру
```

```text
app → db:5432
→ связь по имени сервиса
```

```text
Named volume
→ постоянные данные PostgreSQL
```

```text
depends_on
→ порядок запуска

service_healthy
→ ожидание готовности сервиса
```

```text
healthcheck
→ проверка реального состояния сервиса
```

```text
restart: unless-stopped
→ автоматический перезапуск
```

```text
ps → logs → exec
→ базовая диагностика
```

```text
stop ≠ down ≠ down -v
```


