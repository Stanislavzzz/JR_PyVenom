# Шпаргалка: PostgreSQL - ALTER TABLE, INSERT, UPDATE и DELETE

## 🛠️ Изменение таблицы: `ALTER TABLE`

`ALTER TABLE` используется для изменения уже существующей таблицы.

С его помощью можно:

```text
добавлять столбцы
переименовывать столбцы
менять тип данных
задавать и удалять DEFAULT
добавлять и удалять ограничения
удалять столбцы
```

---

# ➕ Добавить новый столбец

```sql
ALTER TABLE training.users
ADD COLUMN phone text;
```

Здесь:

```text
training.users → изменяемая таблица
phone          → новый столбец
text           → тип данных
```

---

# ➕ Добавить столбец с `NOT NULL` и `DEFAULT`

```sql
ALTER TABLE training.users
ADD COLUMN language text
    NOT NULL
    DEFAULT 'ru';
```

Если значение `language` не передано, PostgreSQL подставит:

```text
ru
```

---

# ✏️ Переименовать столбец

```sql
ALTER TABLE training.users
RENAME COLUMN phone TO contact_phone;
```

Было:

```text
phone
```

Стало:

```text
contact_phone
```

---

# ⚙️ Изменить `DEFAULT`

## Установить новое значение по умолчанию

```sql
ALTER TABLE training.orders
ALTER COLUMN status
SET DEFAULT 'created';
```

---

## Удалить `DEFAULT`

```sql
ALTER TABLE training.orders
ALTER COLUMN status
DROP DEFAULT;
```

---

## Снова задать `DEFAULT`

```sql
ALTER TABLE training.orders
ALTER COLUMN status
SET DEFAULT 'new';
```

---

# 🚫 Добавить `NOT NULL`

```sql
ALTER TABLE training.users
ALTER COLUMN contact_phone
SET NOT NULL;
```

Теперь `contact_phone` не может содержать `NULL`.

Важно: если в таблице уже есть строки с `NULL`, PostgreSQL не позволит добавить `NOT NULL`, пока эти значения не будут исправлены.

---

# ✅ Добавить ограничение `CHECK`

```sql
ALTER TABLE training.orders
ADD CONSTRAINT chk_orders_status
CHECK (
    status IN ('new', 'paid', 'cancelled')
);
```

Разрешены только значения:

```text
new
paid
cancelled
```

Имя ограничения:

```text
chk_orders_status
```

---

# 🗑️ Удалить ограничение

```sql
ALTER TABLE training.orders
DROP CONSTRAINT chk_orders_status;
```

---

# 🗑️ Удалить столбец

```sql
ALTER TABLE training.users
DROP COLUMN IF EXISTS language;
```

`IF EXISTS` означает:

```text
если столбец существует — удалить
если его нет — не выдавать ошибку
```

---

# 🔄 Изменить тип столбца

```sql
ALTER TABLE training.users
ALTER COLUMN user_name
TYPE varchar(100);
```

Было:

```text
text
```

Стало:

```text
varchar(100)
```

Теперь длина значения ограничена `100` символами.

---

# 🗑️ Удалить таблицу

```sql
DROP TABLE IF EXISTS training.contacts;
```

Удаляется таблица `training.contacts`.

---

# ➕ Добавление данных: `INSERT INTO`

## Добавить одну строку

```sql
INSERT INTO training.users (
    user_name,
    email,
    age,
    birth_date,
    contact_phone
)
VALUES (
    'Bob',
    'bob@mail.ru',
    31,
    '1999-01-03',
    '1234567'
);
```

Сначала указываются столбцы, затем значения.

Порядок значений должен соответствовать порядку столбцов.

---

# 📌 Порядок столбцов можно менять

```sql
INSERT INTO training.users (
    email,
    birth_date,
    age,
    contact_phone,
    user_name
)
VALUES (
    'anna@mail.com',
    '2001-07-05',
    27,
    '7654321',
    'Anna'
);
```

Главное — чтобы каждое значение соответствовало столбцу на той же позиции.

---

# ➕ Добавить несколько строк

```sql
INSERT INTO training.users (
    user_name,
    email,
    age,
    birth_date,
    contact_phone
)
VALUES
    (
        'Mary',
        'mary@mail.ru',
        35,
        '1995-10-03',
        '3456789'
    ),
    (
        'Ivan',
        'ivan@mail.ru',
        37,
        '1993-12-15',
        '9875763'
    );
```

После `VALUES` можно перечислить несколько наборов значений через запятую.

---

# 💰 Добавить явное значение `balance`

```sql
INSERT INTO training.users (
    user_name,
    email,
    age,
    birth_date,
    contact_phone,
    balance
)
VALUES (
    'John',
    'john@mail.ru',
    32,
    '1992-10-03',
    '2256789',
    100.12
);
```

---

# ⚙️ Использовать `DEFAULT`

```sql
INSERT INTO training.users (
    user_name,
    email,
    age,
    birth_date,
    contact_phone,
    balance
)
VALUES (
    'Sara',
    'sara@mail.ru',
    45,
    '1984-10-03',
    '3333789',
    DEFAULT
);
```

`DEFAULT` означает: использовать значение по умолчанию, заданное для столбца.

Если для `balance` задано:

```sql
DEFAULT 0
```

то будет записано `0`.

---

# ↩️ `RETURNING`

`RETURNING` позволяет сразу получить данные добавленной строки.

## Вернуть только `user_id`

```sql
INSERT INTO training.users (
    user_name,
    email,
    age,
    birth_date,
    contact_phone,
    balance
)
VALUES (
    'Max',
    'max@mail.ru',
    41,
    '1985-10-03',
    '4444789',
    150.07
)
RETURNING user_id;
```

Это удобно, если `user_id` создаётся автоматически.

---

## Вернуть несколько столбцов

```sql
INSERT INTO training.users (
    user_name,
    email,
    age,
    birth_date,
    contact_phone,
    balance
)
VALUES (
    'Anton',
    'ant@mail.ru',
    21,
    '2005-10-03',
    '5555589',
    450.07
)
RETURNING user_id, user_name, email, balance;
```

---

# 📋 Проверить данные

```sql
SELECT *
FROM training.users;
```

---

# ✏️ Изменение данных: `UPDATE`

## Изменить все строки

```sql
UPDATE training.users
SET balance = 1000;
```

Важно: `WHERE` отсутствует, поэтому изменятся **все строки** таблицы.

---

# 🎯 `UPDATE` с `WHERE`

```sql
UPDATE training.users
SET balance = 2500
WHERE email = 'sara@mail.ru';
```

Изменится только строка, где:

```text
email = sara@mail.ru
```

---

# ➕ Увеличить текущее значение

Корректный синтаксис PostgreSQL:

```sql
UPDATE training.users
SET balance = balance + 1000;
```

Например:

```text
500  → 1500
1000 → 2000
```

---

# ⚠️ Важный момент: `+=` в PostgreSQL нет

Такой вариант:

```sql
UPDATE training.users
SET balance += 1000;
```

в PostgreSQL не работает.

Нужно писать:

```sql
UPDATE training.users
SET balance = balance + 1000;
```

---

# ✏️ Изменить несколько столбцов

```sql
UPDATE training.users
SET
    user_name = 'Bobs',
    age = age + 1,
    is_active = FALSE,
    balance = balance + 1000
WHERE user_name = 'Bob';
```

Одновременно:

```text
user_name → меняется на Bobs
age       → увеличивается на 1
is_active → становится FALSE
balance   → увеличивается на 1000
```

---

# ↩️ `UPDATE ... RETURNING`

```sql
UPDATE training.users
SET
    user_name = 'Bob1',
    age = age + 1,
    is_active = TRUE,
    balance = balance + 2000
WHERE user_name = 'Bobs'
RETURNING *;
```

`RETURNING *` возвращает всю изменённую строку.

Можно вернуть только нужные поля:

```sql
RETURNING user_id, user_name, balance;
```

---

# 🗑️ Удаление данных: `DELETE`

## Удалить конкретную строку

```sql
DELETE FROM training.users
WHERE user_id = 2;
```

Удаляется только строка, где `user_id = 2`.

---

# ↩️ `DELETE ... RETURNING`

```sql
DELETE FROM training.users
WHERE user_id = 10
RETURNING user_name, email, age;
```

Строка удаляется, но PostgreSQL сразу возвращает её данные.

---

# ⚠️ Удалить все строки

```sql
DELETE FROM training.users;
```

Так как `WHERE` отсутствует, удаляются **все строки** таблицы.

Сама таблица остаётся.

---

# ⚖️ `DELETE` и `DROP TABLE`

```sql
DELETE FROM training.users;
```

Удаляет данные, но таблица остаётся.

А:

```sql
DROP TABLE training.users;
```

удаляет саму таблицу.
