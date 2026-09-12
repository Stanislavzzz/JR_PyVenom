# Шпаргалка
# PostgreSQL — агрегаты, GROUP BY, HAVING, подзапросы, CTE и UNION  
  
## 🔗 Полезная ссылка

### Практика SQL

```text
https://sql-ex.ru/?Lang=0
```

---

# 🚫 Проверка `NULL`

## Найти строки, где значение не `NULL`

```sql
SELECT *
FROM flights
WHERE actual_departure IS NOT NULL;
```

Условие:

```sql
actual_departure IS NOT NULL
```

означает: поле `actual_departure` содержит значение.

Для `NULL` используются:

```sql
IS NULL
IS NOT NULL
```

Не нужно писать:

```sql
= NULL
!= NULL
```

---

# 🧩 Условная логика: `CASE`

`CASE` позволяет создать значение в зависимости от условий.

```sql
SELECT
    model,
    range,
    CASE
        WHEN range >= 10000 THEN 'Дальний'
        WHEN range >= 5000 THEN 'Средний'
        ELSE 'Ближний'
    END AS range_category
FROM airplanes
ORDER BY range DESC;
```

Логика:

```text
range >= 10000  → Дальний
range >= 5000   → Средний
иначе           → Ближний
```

Общая структура:

```sql
CASE
    WHEN условие_1 THEN результат_1
    WHEN условие_2 THEN результат_2
    ELSE результат_3
END
```

Псевдоним результата:

```sql
END AS range_category
```

---

# 🔢 Агрегатные функции

Агрегатные функции работают сразу с набором строк и возвращают итоговое значение.

Основные функции занятия:

```text
COUNT()
SUM()
AVG()
MIN()
MAX()
```

---

# 🔢 `COUNT(*)`

## Посчитать количество строк

```sql
SELECT
    COUNT(*)
FROM bookings;
```

`COUNT(*)` считает все строки таблицы.

---

# 🔢 `COUNT(column)`

```sql
SELECT
    COUNT(actual_departure) AS dep
FROM flights;
```

`COUNT(actual_departure)` считает только строки, где `actual_departure` не равен `NULL`.

Сравнение:

```text
COUNT(*)       → считает все строки
COUNT(column)  → считает только не-NULL значения столбца
```

---

# ♻️ `COUNT(DISTINCT ...)`

## Посчитать количество уникальных стран

```sql
SELECT
    COUNT(DISTINCT country) AS d_c
FROM airports;
```

`DISTINCT country` оставляет уникальные страны, а `COUNT(...)` считает их количество.

---

# ➕ `SUM`

```sql
SELECT
    SUM(total_amount)
FROM bookings;
```

`SUM()` возвращает сумму значений столбца.

---

# 📊 `AVG`

```sql
SELECT
    AVG(total_amount)
FROM bookings;
```

`AVG()` возвращает среднее арифметическое.

---

# 🔽 `MIN`

```sql
SELECT
    MIN(total_amount)
FROM bookings;
```

`MIN()` возвращает минимальное значение.

---

# 🔼 `MAX`

```sql
SELECT
    MAX(total_amount)
FROM bookings;
```

`MAX()` возвращает максимальное значение.

---

# 🔼🔽 Несколько агрегатов одновременно

```sql
SELECT
    MAX(total_amount),
    MIN(total_amount)
FROM bookings;
```

В одном `SELECT` можно использовать несколько агрегатных функций.

---

# 📦 Группировка: `GROUP BY`

`GROUP BY` объединяет строки в группы.

```sql
SELECT
    fare_conditions,
    COUNT(*) AS segments_count,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM segments
GROUP BY fare_conditions;
```

Строки группируются по:

```sql
fare_conditions
```

Например:

```text
Economy
Comfort
Business
```

Для каждой группы отдельно вычисляются:

```text
COUNT(*)
AVG(price)
MIN(price)
MAX(price)
```

---

# 📌 Что выводят при `GROUP BY`

Если используется:

```sql
GROUP BY fare_conditions
```

то в `SELECT` можно выводить поле группировки:

```sql
fare_conditions
```

и агрегатные функции:

```sql
COUNT(...)
SUM(...)
AVG(...)
MIN(...)
MAX(...)
```

---

# ⏱️ `WHERE` перед группировкой

```sql
SELECT
    status,
    COUNT(*) AS count_f
FROM flights
WHERE scheduled_departure > bookings.now()
GROUP BY status
ORDER BY count_f;
```

Сначала:

```sql
WHERE scheduled_departure > bookings.now()
```

отбирает нужные строки.

После этого:

```sql
GROUP BY status
```

группирует оставшиеся строки.

---

# 🕒 `bookings.now()`

В учебной базе используется функция:

```sql
bookings.now()
```

Пример:

```sql
SELECT *
FROM flights
WHERE scheduled_departure > bookings.now();
```

Запрос выбирает рейсы, у которых плановое время вылета позже текущего времени учебной базы.

---

# 🎯 Фильтрация групп: `HAVING`

`HAVING` используется после `GROUP BY` для фильтрации групп.

```sql
SELECT
    status,
    COUNT(*) AS count_f
FROM flights
WHERE scheduled_departure > bookings.now()
GROUP BY status
HAVING COUNT(*) > 15
ORDER BY count_f;
```

Условие:

```sql
HAVING COUNT(*) > 15
```

оставляет только группы, где количество строк больше `15`.

---

# ⚖️ `WHERE` и `HAVING`

Главное отличие:

```text
WHERE   → фильтрует отдельные строки до GROUP BY
HAVING  → фильтрует группы после GROUP BY
```

Пример:

```sql
WHERE scheduled_departure > bookings.now()
```

сначала отбирает рейсы.

Потом:

```sql
GROUP BY status
```

создаёт группы.

И только затем:

```sql
HAVING COUNT(*) > 15
```

отбирает нужные группы.

---

# 📌 `HAVING` и агрегаты

Чаще всего `HAVING` используют с агрегатами:

```sql
HAVING COUNT(*) > 15
```

Но `HAVING` не обязан состоять только из агрегатных функций.

Главная идея:

```text
WHERE  → условие для строк
HAVING → условие для групп
```

---

# 📥 Подзапрос

Подзапрос — это запрос внутри другого запроса.

```sql
SELECT
    *
FROM bookings
WHERE total_amount > (
    SELECT
        AVG(total_amount)
    FROM bookings
)
ORDER BY total_amount ASC;
```

Внутренний запрос:

```sql
SELECT
    AVG(total_amount)
FROM bookings
```

сначала вычисляет среднюю сумму бронирования.

После этого внешний запрос выбирает строки, где:

```sql
total_amount > среднее_значение
```

---

# 🧭 Как выполняется подзапрос

Упрощённо:

```text
1. Выполняется внутренний SELECT
2. Получается среднее значение
3. Значение используется во внешнем WHERE
4. Выполняется внешний SELECT
```

---

# 🧱 CTE: `WITH`

`WITH` позволяет создать временный именованный результат запроса.

```sql
WITH exp_booking AS (
    SELECT
        book_ref,
        book_date,
        total_amount
    FROM bookings
    WHERE total_amount > 30000
)

SELECT
    book_ref,
    total_amount
FROM exp_booking
ORDER BY total_amount DESC;
```

Сначала создаётся временный результат:

```sql
WITH exp_booking AS (...)
```

Потом к нему можно обращаться почти как к таблице:

```sql
FROM exp_booking
```

CTE существует только во время выполнения текущего SQL-запроса.

---

# 🏷️ Имя CTE

В примере:

```sql
exp_booking
```

это имя временного результата.

Внутри него:

```sql
SELECT
    book_ref,
    book_date,
    total_amount
FROM bookings
WHERE total_amount > 30000
```

---

# 🧱 Несколько CTE

В одном `WITH` можно создать несколько CTE.

```sql
WITH fare_stats_one AS (
    SELECT
        fare_conditions,
        COUNT(*) AS s_count,
        AVG(price) AS a_price
    FROM segments
    GROUP BY fare_conditions
),

fare_stats_two AS (
    SELECT
        fare_conditions,
        COUNT(*) AS s_count,
        AVG(price) AS a_price
    FROM segments
    GROUP BY fare_conditions
)

SELECT
    fare_conditions,
    a_price
FROM fare_stats_two
WHERE a_price > 6000;
```

CTE разделяются запятыми:

```sql
WITH cte_1 AS (...),
     cte_2 AS (...)
```

После создания CTE можно работать с ним как с обычным результатом запроса.

---

# 🔗 Объединение результатов: `UNION ALL`

`UNION ALL` объединяет результаты двух запросов.

```sql
SELECT
    route_no
FROM flights
WHERE status = 'Delayed'

UNION ALL

SELECT
    route_no
FROM flights
WHERE status = 'Cancelled';
```

Результаты обоих `SELECT` складываются вместе.

Повторы сохраняются.

---

# 🔗 `UNION`

`UNION` также объединяет результаты нескольких `SELECT`.

```sql
SELECT
    route_no
FROM flights
WHERE status = 'Delayed'

UNION

SELECT
    route_no
FROM flights
WHERE status = 'Delayed';
```

`UNION` удаляет повторяющиеся строки.

---

# ⚖️ `UNION` и `UNION ALL`

```text
UNION
    → объединяет результаты
    → удаляет дубликаты

UNION ALL
    → объединяет результаты
    → сохраняет дубликаты
```

Если удалять дубликаты не требуется, обычно используют `UNION ALL`.

---

# 📌 Требования для `UNION`

Объединяемые запросы должны возвращать одинаковое количество столбцов.

Например:

```sql
SELECT route_no
...
UNION
SELECT route_no
...
```

Типы данных соответствующих столбцов должны быть совместимы.

---

# 🧭 Логика запроса с группировкой

Пример:

```sql
SELECT
    status,
    COUNT(*) AS count_f
FROM flights
WHERE scheduled_departure > bookings.now()
GROUP BY status
HAVING COUNT(*) > 15
ORDER BY count_f;
```

Упрощённый порядок выполнения:

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
```

То есть:

1. берём строки из таблицы;
2. фильтруем через `WHERE`;
3. группируем через `GROUP BY`;
4. фильтруем группы через `HAVING`;
5. формируем результат через `SELECT`;
6. сортируем через `ORDER BY`.

---
