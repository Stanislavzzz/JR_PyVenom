# Шпаргалка: PostgreSQL - схемы, таблицы, типы данных и ограничения

## 🗂️ Схемы в PostgreSQL

Схема - это пространство имён внутри базы данных.

Она позволяет логически разделять таблицы и другие объекты.

Например:

```text
bookings.flights
training.users
training.orders
```

Здесь:

```text
bookings
training
```

— имена схем.

А:

```text
flights
users
orders
```

— имена таблиц.

---

# 🔍 Посмотреть список схем

```sql
SELECT
    schema_name
FROM information_schema.schemata;
```

Запрос выводит список схем текущей базы данных.

---

# ➕ Создать схему

```sql
CREATE SCHEMA IF NOT EXISTS training;
```

Обозначения:

* `CREATE SCHEMA` — создать схему;
* `training` — имя схемы;
* `IF NOT EXISTS` — не выдавать ошибку, если схема уже существует.

---

# 🔎 Проверить существование схемы

```sql
SELECT
    schema_name
FROM information_schema.schemata
WHERE schema_name = 'training';
```

Если схема существует, запрос вернёт:

```text
training
```

---

# 🧭 `search_path`

PostgreSQL использует `search_path`, чтобы понимать, в каких схемах искать таблицы, если схема явно не указана.

Посмотреть текущий `search_path`:

```sql
SHOW search_path;
```

---

# 📋 Таблица без указания схемы

```sql
SELECT *
FROM flights;
```

PostgreSQL ищет таблицу `flights` по схемам, указанным в `search_path`.

---

# 📋 Явное указание схемы

```sql
SELECT *
FROM bookings.flights;
```

Здесь схема указана явно:

```text
bookings
```

Полное имя объекта:

```text
схема.таблица
```

Например:

```text
bookings.flights
training.users
training.orders
```

---

# 🏗️ Создание таблицы: `CREATE TABLE`

Простой пример:

```sql
CREATE TABLE training.users (
    user_id bigint,
    user_name text,
    age integer
);
```

Здесь создаётся таблица:

```text
training.users
```

со столбцами:

```text
user_id
user_name
age
```

---

# 🏗️ Ещё одна таблица

```sql
CREATE TABLE training.contacts (
    email text
);
```

Создаётся таблица:

```text
training.contacts
```

с одним столбцом:

```text
email
```

---

# 🗑️ Удаление таблицы: `DROP TABLE`

```sql
DROP TABLE IF EXISTS training.users;
```

Обозначения:

* `DROP TABLE` — удалить таблицу;
* `IF EXISTS` — не выдавать ошибку, если таблицы нет.

---

# 📦 Основные типы данных

На занятии использовали:

```sql
CREATE TABLE training.users (
    user_id bigint,
    user_name text,
    email text,
    age integer,
    balance numeric(12, 2),
    is_active boolean,
    birth_date date,
    created_at timestamptz,
    external_id uuid,
    profile jsonb
);
```

---

# 🔢 `bigint`

```sql
user_id bigint
```

Тип для целых чисел большого диапазона.

Подходит, например, для идентификаторов.

---

# 📝 `text`

```sql
user_name text
```

Строковый тип данных.

Используется для текста произвольной длины.

---

# 🔢 `integer`

```sql
age integer
```

Тип для целых чисел.

---

# 💰 `numeric(12, 2)`

```sql
balance numeric(12, 2)
```

Точное числовое значение.

Здесь:

```text
12 → общее количество цифр
2  → количество цифр после запятой
```

Например:

```text
12345.67
```

---

# ✅ `boolean`

```sql
is_active boolean
```

Логический тип.

Основные значения:

```text
TRUE
FALSE
NULL
```

---

# 📅 `date`

```sql
birth_date date
```

Хранит дату без времени.

Например:

```text
2026-09-18
```

---

# 🕒 `timestamptz`

```sql
created_at timestamptz
```

Хранит дату и время с учётом часового пояса.

---

# 🆔 `uuid`

```sql
external_id uuid
```

Тип для UUID-идентификаторов.

Пример значения:

```text
550e8400-e29b-41d4-a716-446655440000
```

---

# 📦 `jsonb`

```sql
profile jsonb
```

Позволяет хранить данные в формате JSON.

Например:

```json
{
  "city": "Moscow",
  "level": "pro"
}
```

---

# 🔍 Посмотреть столбцы таблицы

```sql
SELECT
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema = 'training'
    AND table_name = 'users';
```

Запрос показывает:

```text
имя столбца
тип данных
```

---

# 🆔 Автоматический идентификатор: `IDENTITY`

```sql
user_id bigint
    GENERATED ALWAYS AS IDENTITY
    PRIMARY KEY
```

`GENERATED ALWAYS AS IDENTITY` означает, что PostgreSQL автоматически создаёт значение идентификатора.

Например:

```text
1
2
3
4
...
```

---

# 🔑 `PRIMARY KEY`

```sql
PRIMARY KEY
```

Первичный ключ:

* однозначно идентифицирует строку;
* должен быть уникальным;
* не может быть `NULL`.

Пример:

```sql
user_id bigint
    GENERATED ALWAYS AS IDENTITY
    PRIMARY KEY
```

---

# 🚫 `NOT NULL`

```sql
user_name text
    NOT NULL
```

Означает, что значение обязательно.

Нельзя оставить поле пустым через `NULL`.

---

# ✅ `CHECK`

`CHECK` задаёт дополнительное условие для значения.

Пример:

```sql
user_name text
    NOT NULL
    CHECK (length(trim(user_name)) > 0)
```

Здесь проверяется, что после удаления пробелов строка не пустая.

---

# 📏 Проверка возраста

```sql
age integer
    NOT NULL
    CHECK (age BETWEEN 0 AND 150)
```

Значение `age` должно находиться в диапазоне:

```text
0 ... 150
```

Границы включаются.

---

# ✉️ `UNIQUE`

```sql
email text
    NOT NULL
    UNIQUE
```

`UNIQUE` запрещает повторяющиеся значения.

То есть два пользователя не смогут иметь одинаковый `email`.

---

# 💰 `DEFAULT`

```sql
balance numeric(12, 2)
    NOT NULL
    DEFAULT 0
    CHECK (balance >= 0)
```

`DEFAULT 0` означает:

если значение `balance` не передано, PostgreSQL автоматически подставит:

```text
0
```

---

# ✅ Значение по умолчанию для `boolean`

```sql
is_active boolean
    NOT NULL
    DEFAULT TRUE
```

Если значение не указано:

```text
is_active = TRUE
```

---

# 🕒 Значение времени по умолчанию

```sql
created_at timestamptz
    NOT NULL
    DEFAULT now()
```

Если `created_at` не указан, PostgreSQL автоматически подставит текущее время.

---

# 🏗️ Таблица `users` с ограничениями

```sql
DROP TABLE IF EXISTS training.users;

CREATE TABLE training.users (
    user_id bigint
        GENERATED ALWAYS AS IDENTITY
        PRIMARY KEY,

    user_name text
        NOT NULL
        CHECK (length(trim(user_name)) > 0),

    email text
        NOT NULL
        UNIQUE,

    age integer
        NOT NULL
        CHECK (age BETWEEN 0 AND 150),

    balance numeric(12, 2)
        NOT NULL
        DEFAULT 0
        CHECK (balance >= 0),

    is_active boolean
        NOT NULL
        DEFAULT TRUE,

    birth_date date,

    created_at timestamptz
        NOT NULL
        DEFAULT now(),

    external_id uuid,

    profile jsonb
);
```

---

# 🔍 Посмотреть структуру столбцов

```sql
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_schema = 'training'
    AND table_name = 'users';
```

Запрос показывает:

```text
column_name    → имя столбца
data_type      → тип данных
is_nullable    → можно ли хранить NULL
column_default → значение по умолчанию
```

---

# 🔗 Внешний ключ: `FOREIGN KEY`

Сначала создаём таблицу `orders`.

```sql
DROP TABLE IF EXISTS training.orders;

CREATE TABLE training.orders (
    order_id bigint
        GENERATED ALWAYS AS IDENTITY
        PRIMARY KEY,

    user_id bigint
        NOT NULL,

    total_amount numeric(12, 2)
        NOT NULL
        CHECK (total_amount >= 0),

    status text
        NOT NULL
        DEFAULT 'new',

    created_at timestamptz
        NOT NULL
        DEFAULT now(),

    CONSTRAINT fk_orders_user
        FOREIGN KEY (user_id)
        REFERENCES training.users(user_id)
        ON DELETE RESTRICT
);
```

---

# 🔑 Что делает `FOREIGN KEY`

```sql
FOREIGN KEY (user_id)
REFERENCES training.users(user_id)
```

Означает:

```text
training.orders.user_id
```

должен ссылаться на существующий:

```text
training.users.user_id
```

Это создаёт связь:

```text
users
  ↓ user_id
orders
```

---

# 🏷️ Имя ограничения: `CONSTRAINT`

```sql
CONSTRAINT fk_orders_user
```

Здесь:

```text
fk_orders_user
```

— имя ограничения внешнего ключа.

Именованные ограничения удобнее искать и изменять позже.

---

# 🚫 `ON DELETE RESTRICT`

```sql
ON DELETE RESTRICT
```

Запрещает удалить пользователя, если на него ссылаются строки в `orders`.

Пример:

```text
users.user_id = 10
```

Если существует заказ:

```text
orders.user_id = 10
```

то удалить такого пользователя нельзя, пока существует связанный заказ.

---

# 🔍 Посмотреть ограничения таблицы

```sql
SELECT
    constraint_name,
    constraint_type
FROM information_schema.table_constraints
WHERE table_schema = 'training'
    AND table_name = 'orders';
```

Запрос показывает ограничения таблицы.

Например:

```text
PRIMARY KEY
FOREIGN KEY
UNIQUE
CHECK
```

---

# 🧭 Общая структура `CREATE TABLE`

```sql
CREATE TABLE schema_name.table_name (
    column_name data_type ограничения,
    column_name data_type ограничения
);
```

Пример:

```sql
CREATE TABLE training.users (
    user_id bigint PRIMARY KEY,
    user_name text NOT NULL,
    age integer CHECK (age >= 0)
);
```

---



