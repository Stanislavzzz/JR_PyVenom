https://www.postgresql.org/
https://www.pgadmin.org/
https://hub.docker.com/r/dpage/pgadmin4/
https://hub.docker.com/_/postgres

docker --version
docker compose logs postgres

docker compose exec postgres pg_isready
docker compose exec postgres psql -U postgres -d postgres -c "SELECT version();"

docker compose config
docker compose up -d
docker compose ps -a

docker compose down
docker compose down -v


gunzip -c ./import/demo-db.sql.gz | docker compose exec -T postgres psql -U postgres


sudo systemctl status postgresql
sudo systemctl stop postgresql
sudo systemctl disable postgresql

docker volume ls
docker network ls
docker system prune -a --volumes
docker network prune
docker volume prune -a
docker volume ls
docker network ls


docker compose logs postgres
docker compose exec postgres pg_isready
docker compose exec postgres psql -U postgres -d postgres -c "SELECT version();"
docker compose logs pgadmin

./import/demo-db.sql | docker compose exec -T postgres psql -U postgres
gunzip -c ./import/demo-db.sql.gz | docker compose exec -T postgres psql -U postgres

http://localhost:5050/
docker compose up -d

===========

# Шпаргалка: PostgreSQL + pgAdmin в Docker Compose

## Полезные ссылки

### PostgreSQL

```text
https://www.postgresql.org/
```

### pgAdmin

```text
https://www.pgadmin.org/
```

### PostgreSQL в Docker Hub

```text
https://hub.docker.com/_/postgres
```

### pgAdmin в Docker Hub

```text
https://hub.docker.com/r/dpage/pgadmin4/
```

---

# Проверка Docker

### Проверить установленную версию Docker

```bash
docker --version
```

---

# Docker Compose

## Проверить `compose.yaml`

```bash
docker compose config
```

Команда проверяет структуру и синтаксис Docker Compose-файла.

---

## Запустить PostgreSQL и pgAdmin

```bash
docker compose up -d
```

`-d` — запустить контейнеры в фоновом режиме.

---

## Проверить контейнеры

```bash
docker compose ps -a
```

Показывает состояние всех контейнеров проекта.

---

## Остановить и удалить контейнеры

```bash
docker compose down
```

Удаляются контейнеры и сеть Compose.

Данные в именованных volumes сохраняются.

---

## Удалить контейнеры вместе с данными

```bash
docker compose down -v
```

`-v` — дополнительно удалить volumes проекта.

Важно:

```text
docker compose down    → данные PostgreSQL сохраняются
docker compose down -v → данные PostgreSQL удаляются
```

---

# Проверка PostgreSQL

## Посмотреть логи PostgreSQL

```bash
docker compose logs postgres
```

Если нужно следить за логами:

```bash
docker compose logs -f postgres
```

Выход:

```text
Ctrl + C
```

---

## Проверить готовность PostgreSQL

```bash
docker compose exec postgres pg_isready
```

Если сервер работает, получим примерно:

```text
/var/run/postgresql:5432 - accepting connections
```

---

## Проверить версию PostgreSQL

```bash
docker compose exec postgres psql -U postgres -d postgres -c "SELECT version();"
```

Обозначения:

* `exec` — выполнить команду внутри контейнера;
* `postgres` — имя сервиса;
* `psql` — консольный клиент PostgreSQL;
* `-U postgres` — пользователь;
* `-d postgres` — база данных;
* `-c` — выполнить SQL-команду.

---

# pgAdmin

## Посмотреть логи pgAdmin

```bash
docker compose logs pgadmin
```

## Открыть pgAdmin

```text
http://localhost:5050/
```

PostgreSQL внутри Docker Compose обычно подключается из pgAdmin по имени сервиса:

```text
postgres
```

а не:

```text
localhost
```

---

# Импорт demo-базы

## Импорт SQL-файла `.sql`

```bash
cat ./import/demo-db.sql | docker compose exec -T postgres psql -U postgres
```

---

## Импорт сжатого файла `.sql.gz`

```bash
gunzip -c ./import/demo-db.sql.gz | docker compose exec -T postgres psql -U postgres
```

Обозначения:

* `gunzip -c` — распаковать архив и вывести содержимое;
* `|` — передать результат следующей команде;
* `exec -T` — выполнить команду без псевдотерминала;
* `psql` — передать SQL-команды PostgreSQL.

Схема:

```text
demo-db.sql.gz
      ↓
   gunzip
      ↓
    psql
      ↓
 PostgreSQL
```

---

# Системный PostgreSQL в Ubuntu

Если PostgreSQL ранее устанавливался непосредственно в Ubuntu, он может конфликтовать с Docker-версией.

## Проверить состояние

```bash
sudo systemctl status postgresql
```

## Остановить PostgreSQL

```bash
sudo systemctl stop postgresql
```

## Отключить автоматический запуск

```bash
sudo systemctl disable postgresql
```

После этого PostgreSQL используем только через Docker Compose.

---

# Docker Volumes

## Посмотреть volumes

```bash
docker volume ls
```

Volume позволяет сохранять данные PostgreSQL независимо от контейнера.

```text
контейнер PostgreSQL
        ↓
      volume
        ↓
данные сохраняются
```

---

## Удалить неиспользуемые volumes

```bash
docker volume prune -a
```

Осторожно: команда удаляет неиспользуемые Docker volumes.

---

# Docker Networks

## Посмотреть Docker-сети

```bash
docker network ls
```

Docker Compose создаёт сеть, через которую контейнеры могут обращаться друг к другу по именам сервисов.

Например:

```text
pgadmin → postgres
```

---

## Удалить неиспользуемые сети

```bash
docker network prune
```

---

# Полная очистка Docker

```bash
docker system prune -a --volumes
```

Удаляет неиспользуемые:

* контейнеры;
* образы;
* сети;
* volumes.

Использовать осторожно.

---

# Быстрая диагностика

Если PostgreSQL не работает:

```bash
# Проверить compose.yaml
docker compose config

# Проверить контейнеры
docker compose ps -a

# Посмотреть логи PostgreSQL
docker compose logs postgres

# Проверить PostgreSQL
docker compose exec postgres pg_isready

# Проверить версию
docker compose exec postgres psql -U postgres -d postgres -c "SELECT version();"

# Посмотреть логи pgAdmin
docker compose logs pgadmin
```

---

# Краткий порядок работы на занятии

```bash
# 1. Запустить PostgreSQL и pgAdmin
docker compose up -d

# 2. Проверить контейнеры
docker compose ps -a

# 3. Проверить PostgreSQL
docker compose exec postgres pg_isready

# 4. При необходимости посмотреть логи
docker compose logs postgres

# 5. Открыть pgAdmin
# http://localhost:5050/
```

Если необходимо остановить проект:

```bash
docker compose down
```

На следующем занятии достаточно снова выполнить:

```bash
docker compose up -d
```

Данные PostgreSQL сохранятся в Docker volume.
