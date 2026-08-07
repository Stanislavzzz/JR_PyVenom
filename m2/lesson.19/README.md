
# Шпаргалка: Docker

## 🐳 Полезные ссылки

### Установка Docker Desktop для Windows

```text
https://docs.docker.com/desktop/setup/install/windows-install/
```

### Скачать Docker Desktop

```text
https://www.docker.com/products/docker-desktop/
```

### Docker Hub — каталог готовых образов

```text
https://hub.docker.com/
```

---

## 🔍 Проверка установки Docker

### Показать установленную версию Docker

```bash
docker --version
```

Команда выводит краткую информацию о версии Docker CLI.

### Показать подробную информацию о Docker

```bash
docker version
```

Команда показывает версии:

* Docker Client;
* Docker Server;
* Docker Engine;
* API Docker.

---

## ✅ Проверка работы Docker

### Запустить тестовый контейнер

```bash
docker run hello-world
```

Docker:

1. ищет образ `hello-world` локально;
2. скачивает его из Docker Hub, если образа нет;
3. создаёт контейнер;
4. запускает контейнер;
5. выводит тестовое сообщение.

---

## 📋 Просмотр контейнеров

### Показать запущенные контейнеры

```bash
docker ps
```

### Показать все контейнеры

```bash
docker ps -a
```

Показывает:

* работающие контейнеры;
* остановленные контейнеры;
* завершившиеся контейнеры.

---

## ▶️ Запуск контейнеров

### Запустить интерактивный контейнер Alpine

```bash
docker run -it --rm alpine:latest sh
```

Обозначения:

* `run` — создать и запустить контейнер;
* `-i` — оставить стандартный ввод открытым;
* `-t` — подключить терминал;
* `--rm` — удалить контейнер после завершения;
* `alpine:latest` — образ и его тег;
* `sh` — запустить командную оболочку внутри контейнера.

Для выхода:

```bash
exit
```

Или:

```text
Ctrl + D
```

### Запустить контейнер Alpine в фоновом режиме

```bash
docker run -d --name my-alpine alpine:latest sleep 3000
```

Обозначения:

* `-d` — запустить контейнер в фоне;
* `--name my-alpine` — присвоить контейнеру имя;
* `alpine:latest` — используемый образ;
* `sleep 3000` — команда внутри контейнера, которая работает 3000 секунд.

---

## ⏹️ Управление контейнерами

### Остановить контейнер

```bash
docker stop 670ae92be6fe
```

Вместо идентификатора можно использовать имя контейнера:

```bash
docker stop my-alpine
```

### Запустить остановленный контейнер

```bash
docker start 670ae92be6fe
```

Или по имени:

```bash
docker start my-alpine
```

### Перезапустить контейнер

```bash
docker restart 670ae92be6fe
```

Или по имени:

```bash
docker restart my-alpine
```

---

## 🗑️ Удаление контейнеров

### Удалить остановленный контейнер

```bash
docker rm my-alpine
```

Работающий контейнер сначала необходимо остановить:

```bash
docker stop my-alpine
docker rm my-alpine
```

---

## 🔎 Поиск образов

### Найти образы Debian в Docker Hub

```bash
docker search debian
```

Команда выводит найденные образы, их описание и популярность.

---

## 📥 Скачивание образов

### Скачать образ Debian

```bash
docker pull debian:11.11-slim
```

Обозначения:

* `debian` — название образа;
* `11.11-slim` — тег образа;
* `slim` — уменьшенная версия образа.

Если тег не указан, Docker обычно использует тег `latest`:

```bash
docker pull debian
```

---

## 🖼️ Просмотр образов

### Показать локальные Docker-образы

```bash
docker images
```

Команда показывает:

* название образа;
* тег;
* идентификатор;
* дату создания;
* размер.

---

## 🧹 Удаление образов

### Удалить образ по идентификатору

```bash
docker rmi 4aaf0b273f92
```

### Удалить образ по имени и тегу

```bash
docker rmi ubuntu:26.04
```

Образ нельзя удалить, если он используется существующим контейнером. Сначала необходимо удалить соответствующий контейнер.

---

## 🧭 Краткий порядок работы

```bash
# Проверить Docker
docker --version

# Скачать образ
docker pull debian:11.11-slim

# Посмотреть образы
docker images

# Запустить контейнер
docker run -it --rm alpine:latest sh

# Запустить контейнер в фоне
docker run -d --name my-alpine alpine:latest sleep 3000

# Посмотреть контейнеры
docker ps
docker ps -a

# Остановить контейнер
docker stop my-alpine

# Запустить контейнер
docker start my-alpine

# Перезапустить контейнер
docker restart my-alpine

# Удалить контейнер
docker rm my-alpine

# Удалить образ
docker rmi debian:11.11-slim
```


## 🔧 Диагностика Docker-контейнера

### Запустить контейнер Alpine в фоновом режиме

```bash
docker run -d --name diag-alpine alpine:latest sleep 3000
```

Обозначения:

* `-d` — запустить контейнер в фоне;
* `--name diag-alpine` — присвоить контейнеру имя;
* `alpine:latest` — используемый образ;
* `sleep 3000` — команда, которая поддерживает контейнер запущенным 3000 секунд.

### Показать логи контейнера

```bash
docker logs diag-alpine
```

Команда выводит сообщения, записанные контейнером в стандартный вывод и поток ошибок.

### Следить за логами контейнера в реальном времени

```bash
docker logs -f diag-alpine
```

Флаг `-f` означает `follow` — продолжать выводить новые сообщения.

Для остановки просмотра логов:

```text
Ctrl + C
```

---

## 💻 Выполнение команд внутри контейнера

### Открыть командную оболочку внутри контейнера

```bash
docker exec -it diag-alpine sh
```

Обозначения:

* `exec` — выполнить команду в работающем контейнере;
* `-i` — оставить стандартный ввод открытым;
* `-t` — подключить терминал;
* `diag-alpine` — имя контейнера;
* `sh` — запустить командную оболочку.

Для выхода из контейнера:

```bash
exit
```

---

## 🔍 Получение информации о контейнере

### Показать подробную информацию о контейнере

```bash
docker inspect diag-alpine
```

Команда выводит информацию в формате JSON:

* идентификатор контейнера;
* используемый образ;
* состояние контейнера;
* настройки сети;
* переменные окружения;
* подключённые директории;
* запущенную команду.

### Вывести только имя контейнера

```bash
docker inspect --format='{{.Name}}' diag-alpine
```

Результат:

```text
/diag-alpine
```

Параметр `--format` позволяет получить только нужное поле из результата `docker inspect`.

---

# 🚀 Подготовка FastAPI-приложения

## Установка зависимостей

### Установить FastAPI

```bash
pip install fastapi
```

### Установить сервер Uvicorn

```bash
pip install uvicorn
```

FastAPI содержит код веб-приложения, а Uvicorn запускает его как веб-сервер.

### Сохранить зависимости проекта

```bash
pip freeze > requirements.txt
```

Пример файла `requirements.txt`:

```text
fastapi==0.116.1
uvicorn==0.35.0
```

Версии могут отличаться в зависимости от даты установки.

---

## Запуск FastAPI без Docker

### Запустить приложение локально

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

Обозначения:

* `main` — файл `main.py`;
* `app` — объект FastAPI внутри файла;
* `--host 127.0.0.1` — приложение доступно только на текущем компьютере;
* `--port 8000` — приложение работает на порту `8000`.

Открыть приложение можно по адресу:

```text
http://127.0.0.1:8000
```

Автоматическая документация FastAPI:

```text
http://127.0.0.1:8000/docs
```

---

# 📝 Файл `main.py`

### Создать простое FastAPI-приложение

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World!&&&&&123456789"}
```

Обозначения:

* `FastAPI()` — создаёт объект веб-приложения;
* `@app.get("/")` — обрабатывает GET-запрос по адресу `/`;
* `hello_world()` — функция обработчика;
* возвращаемый словарь автоматически преобразуется в JSON.

---

# 🐳 Dockerfile

### Создать файл `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Выбрать базовый образ

```dockerfile
FROM python:3.12-slim
```

Используется облегчённый образ с Python 3.12.

### Установить рабочую директорию

```dockerfile
WORKDIR /app
```

Все следующие команды будут выполняться внутри директории `/app`.

### Скопировать файл зависимостей

```dockerfile
COPY requirements.txt .
```

Файл `requirements.txt` копируется в `/app`.

### Установить зависимости

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Обозначения:

* `RUN` — выполнить команду во время сборки образа;
* `--no-cache-dir` — не сохранять кеш установочных файлов;
* `-r requirements.txt` — установить зависимости из файла.

### Скопировать файлы проекта

```dockerfile
COPY . .
```

Все файлы текущей директории копируются внутрь `/app`.

### Указать порт приложения

```dockerfile
EXPOSE 8000
```

Инструкция показывает, что приложение использует порт `8000`.

Она сама по себе не открывает порт на компьютере.

### Указать команду запуска

```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Адрес `0.0.0.0` обязателен внутри контейнера, чтобы приложение принимало подключения извне.

---

# 🙈 Файл `.dockerignore`

### Исключить ненужные файлы из Docker-образа

```text
.venv/
_old/
.env
*.log
```

Обозначения:

* `.venv/` — локальное виртуальное окружение;
* `_old/` — архивная директория;
* `.env` — файл с секретными переменными;
* `*.log` — все файлы логов.

Эти файлы не будут отправляться в контекст сборки и попадать в Docker-образ.

---

# 🏗️ Сборка Docker-образа

### Собрать образ FastAPI-приложения

```bash
docker build -t demo-fastapi .
```

Обозначения:

* `build` — собрать Docker-образ;
* `-t demo-fastapi` — присвоить образу имя;
* `.` — использовать текущую директорию как контекст сборки.

---

# ▶️ Запуск FastAPI-контейнера

### Запустить приложение в фоновом режиме

```bash
docker run -d -p 8000:8000 --name my_fastapi1 demo-fastapi
```

Обозначения:

* `-d` — запустить контейнер в фоне;
* `-p 8000:8000` — связать порт компьютера с портом контейнера;
* `--name my_fastapi1` — присвоить контейнеру имя;
* `demo-fastapi` — образ, из которого создаётся контейнер.

Схема проброса портов:

```text
порт компьютера:порт контейнера
8000:8000
```

После запуска приложение доступно по адресу:

```text
http://127.0.0.1:8000
```

Документация FastAPI:

```text
http://127.0.0.1:8000/docs
```

---

## 🧭 Краткий порядок работы

```bash
# Установить зависимости
pip install fastapi
pip install uvicorn

# Сохранить зависимости
pip freeze > requirements.txt

# Проверить приложение без Docker
uvicorn main:app --host 127.0.0.1 --port 8000

# Собрать Docker-образ
docker build -t demo-fastapi .

# Запустить контейнер
docker run -d -p 8000:8000 --name my_fastapi1 demo-fastapi

# Посмотреть запущенные контейнеры
docker ps

# Посмотреть логи приложения
docker logs my_fastapi1

# Следить за логами
docker logs -f my_fastapi1

# Получить информацию о контейнере
docker inspect my_fastapi1

# Остановить контейнер
docker stop my_fastapi1

# Удалить контейнер
docker rm my_fastapi1
```

# 💾 Хранение данных в Docker

## 📂 Файлы внутри контейнера

Файлы, созданные внутри контейнера, принадлежат этому контейнеру.

```bash
docker exec message-container ls -la /app/data
````

### Прочитать файл

```bash
docker exec message-container cat /app/data/messages.txt
```

### Запустить Python-скрипт внутри контейнера

```bash
docker exec message-container python storage_app.py "Новое сообщение"
```

### Открыть терминал контейнера

```bash
docker exec -it message-container sh
```

Для выхода:

```bash
exit
```

---

## 🔄 Остановка и удаление контейнера

### Остановить контейнер

```bash
docker stop message-container
```

Данные внутри контейнера сохраняются.

### Запустить тот же контейнер

```bash
docker start message-container
```

Файлы внутри контейнера останутся.

### Удалить контейнер

```bash
docker rm message-container
```

После удаления данные, сохранённые только внутри контейнера, теряются.

Важно:

```text
docker stop  → контейнер и данные остаются
docker start → запускается тот же контейнер
docker rm    → контейнер и его внутренние данные удаляются
docker run   → создаётся новый контейнер
```

---

## 🔍 Проверка подключённых хранилищ

```bash
docker inspect message-container --format "{{json .Mounts}}"
```

Если ничего не подключено:

```text
[]
```

---

# 📁 Bind mount

Bind mount подключает папку компьютера внутрь контейнера.

```bash
docker run -v ./data:/app/data -d --name message-container message-app:1.1
```

Формат:

```text
папка_на_компьютере:папка_в_контейнере
```

Пример:

```text
./data:/app/data
```

Теперь файл:

```text
./data/messages.txt
```

на компьютере соответствует:

```text
/app/data/messages.txt
```

в контейнере.

После удаления контейнера файлы в `./data` сохраняются.

---

## 🐧 Bind mount в Ubuntu

### Через относительный путь

```bash
-v ./data:/app/data
```

### Через абсолютный путь текущего каталога

```bash
-v "$(pwd)/data:/app/data"
```

Проверить текущий каталог:

```bash
pwd
```

---

## 🪟 Bind mount в PowerShell

```powershell
-v "${PWD}/data:/app/data"
```

Например:

```powershell
docker run -v "${PWD}/data:/app/data" -d --name message-container message-app:1.1
```

---

# 🔒 Bind mount только для чтения

Добавляем `:ro`:

```bash
-v ./config:/app/config:ro
```

Пример:

```bash
docker run -v "$(pwd)/config:/app/config:ro" -d --name message-container message-app:1.1
```

Контейнер сможет читать файлы:

```bash
docker exec message-container cat /app/config/settings.txt
```

Но не сможет их изменить.

---

## 🧭 Краткий порядок работы

```bash
# Запустить контейнер с bind mount
docker run -v "$(pwd)/data:/app/data" -d --name message-container message-app:1.1

# Проверить mount
docker inspect message-container --format "{{json .Mounts}}"

# Записать данные
docker exec message-container python storage_app.py "Новое сообщение"

# Прочитать файл внутри контейнера
docker exec message-container cat /app/data/messages.txt

# Проверить файл на компьютере
cat data/messages.txt

# Остановить контейнер
docker stop message-container

# Запустить снова
docker start message-container

# Удалить контейнер
docker rm -f message-container
```

---

## 📌 Главное

```text
Без mount:
данные находятся внутри контейнера
docker rm → данные теряются

Bind mount:
данные находятся в папке компьютера
docker rm → данные сохраняются
```

```
