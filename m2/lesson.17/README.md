
# Docker

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
