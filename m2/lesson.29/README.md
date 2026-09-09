# Шпаргалка: PostgreSQL — JOIN и объединение таблиц

## 🔗 Зачем нужен `JOIN`

`JOIN` позволяет получать связанные данные сразу из нескольких таблиц.

Например:

```text
bookings → tickets
```

Связь выполняется по общему полю:

```text
book_ref
```

Пример:

```sql
SELECT
    bookings.book_ref,
    bookings.book_date,
    tickets.passenger_name
FROM bookings
INNER JOIN tickets
    ON bookings.book_ref = tickets.book_ref
LIMIT 100;
```

Что происходит:

1. берём данные из `bookings`;
2. присоединяем таблицу `tickets`;
3. связываем строки по `book_ref`;
4. выводим нужные столбцы;
5. ограничиваем результат до `100` строк.

---

# 📌 Полное имя столбца

Если запрос работает с несколькими таблицами, удобно явно указывать:

```text
таблица.столбец
```

Например:

```sql
bookings.book_ref
tickets.passenger_name
```

Это особенно важно, если одинаковое имя столбца встречается в нескольких таблицах.

---

# 🏷️ Алиасы таблиц: `AS`

Чтобы не писать полное имя таблицы каждый раз, можно задать псевдоним.

```sql
SELECT
    b.book_ref,
    b.book_date,
    t.passenger_name
FROM bookings AS b
INNER JOIN tickets AS t
    ON b.book_ref = t.book_ref
LIMIT 10;
```

Здесь:

```text
bookings → b
tickets  → t
```

После этого можно писать:

```sql
b.book_ref
t.passenger_name
```

вместо:

```sql
bookings.book_ref
tickets.passenger_name
```

---

# ✂️ Алиасы без `AS`

Для таблиц `AS` можно не писать.

```sql
SELECT
    b.book_ref,
    b.book_date,
    t.passenger_name
FROM bookings b
INNER JOIN tickets t
    ON b.book_ref = t.book_ref
LIMIT 15;
```

Эти записи эквивалентны:

```sql
FROM bookings AS b
```

и:

```sql
FROM bookings b
```

---

# 🔵 `INNER JOIN`

`INNER JOIN` возвращает только те строки, для которых найдено совпадение в обеих таблицах.

```sql
SELECT
    b.book_ref,
    b.book_date,
    t.passenger_name,
    b.total_amount
FROM bookings b
INNER JOIN tickets t
    ON b.book_ref = t.book_ref
WHERE b.total_amount < 700000
ORDER BY b.total_amount DESC
LIMIT 15;
```

Условие соединения:

```sql
ON b.book_ref = t.book_ref
```

---

# 🔵 `JOIN` и `INNER JOIN`

Обычный `JOIN` означает `INNER JOIN`.

То есть:

```sql
INNER JOIN tickets t
    ON b.book_ref = t.book_ref
```

и:

```sql
JOIN tickets t
    ON b.book_ref = t.book_ref
```

работают одинаково.

Пример:

```sql
SELECT
    b.book_ref,
    b.book_date,
    t.passenger_name,
    b.total_amount
FROM bookings b
JOIN tickets t
    ON b.book_ref = t.book_ref
WHERE b.total_amount < 700000
ORDER BY b.total_amount DESC
LIMIT 15;
```

---

# 🔗 Несколько `JOIN` подряд

Можно последовательно объединять несколько таблиц.

На занятии использовали цепочку:

```text
bookings
   ↓ book_ref
tickets
   ↓ ticket_no
segments
   ↓ flight_id
flights
```

Запрос:

```sql
SELECT *
FROM bookings b
JOIN tickets t
    ON b.book_ref = t.book_ref
JOIN segments s
    ON t.ticket_no = s.ticket_no
JOIN flights f
    ON s.flight_id = f.flight_id
WHERE b.total_amount < 700000
  AND b.book_ref = 'JU35I4'
ORDER BY b.total_amount DESC
LIMIT 15;
```

Связи:

```sql
b.book_ref = t.book_ref
```

```sql
t.ticket_no = s.ticket_no
```

```sql
s.flight_id = f.flight_id
```

Каждый следующий `JOIN` добавляет данные ещё одной таблицы.

---

# 📋 `SELECT *` при `JOIN`

Можно вывести все столбцы объединённых таблиц:

```sql
SELECT *
FROM bookings b
JOIN tickets t
    ON b.book_ref = t.book_ref;
```

Или выбрать только нужные:

```sql
SELECT
    b.book_ref,
    b.book_date,
    t.passenger_name,
    b.total_amount
FROM bookings b
JOIN tickets t
    ON b.book_ref = t.book_ref;
```

Второй вариант обычно удобнее: результат получается компактнее и понятнее.

---

# 🔎 `WHERE` после `JOIN`

После объединения таблиц можно фильтровать результат.

```sql
SELECT
    b.book_ref,
    b.book_date,
    t.passenger_name,
    b.total_amount
FROM bookings b
JOIN tickets t
    ON b.book_ref = t.book_ref
WHERE b.total_amount < 700000
ORDER BY b.total_amount DESC
LIMIT 15;
```

Условие:

```sql
WHERE b.total_amount < 700000
```

оставляет только нужные строки.

---

# 🔀 Несколько условий в `WHERE`

```sql
WHERE b.total_amount < 700000
  AND b.book_ref = 'JU35I4'
```

Оба условия должны выполняться одновременно.

---

# ✈️ Объединение `airplanes` и `seats`

```sql
SELECT *
FROM airplanes AS a
JOIN seats AS s
    ON a.airplane_code = s.airplane_code
ORDER BY
    a.airplane_code,
    s.seat_no;
```

Связь:

```sql
a.airplane_code = s.airplane_code
```

Кресла связываются с самолётом по коду самолёта.

---

# ↕️ `ORDER BY` после `JOIN`

Сортировать можно по столбцам из разных таблиц.

```sql
ORDER BY
    a.airplane_code,
    s.seat_no;
```

Если направление не указано, используется сортировка по возрастанию.

Можно указать явно:

```sql
ORDER BY
    s.seat_no DESC,
    a.airplane_code;
```

Здесь:

1. сначала сортировка по `seat_no` по убыванию;
2. затем по `airplane_code`.

---

# 🟡 `LEFT JOIN`

`LEFT JOIN` сохраняет все строки из левой таблицы.

```sql
SELECT *
FROM airplanes AS a
LEFT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
ORDER BY
    s.seat_no DESC,
    a.airplane_code;
```

Левая таблица:

```text
airplanes
```

Правая таблица:

```text
seats
```

Если соответствующей строки в `seats` нет, поля правой таблицы будут содержать `NULL`.

---

# 🟡 `LEFT JOIN` с `airplanes_data`

На занятии также использовался такой запрос:

```sql
SELECT *
FROM airplanes_data AS a
LEFT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
ORDER BY
    s.seat_no DESC,
    a.airplane_code;
```

Здесь левая сторона объединения — `airplanes_data`.

---

# 🔍 Поиск строк без соответствия через `LEFT JOIN`

```sql
SELECT *
FROM airplanes AS a
LEFT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
WHERE s.seat_no IS NULL
ORDER BY
    a.airplane_code;
```

Логика:

1. `LEFT JOIN` сохраняет все самолёты;
2. если места для самолёта не нашлись, поля `seats` будут `NULL`;
3. `WHERE s.seat_no IS NULL` оставляет только такие строки.

Общая схема:

```sql
LEFT JOIN правая_таблица
    ON условие
WHERE правая_таблица.поле IS NULL
```

Так можно искать строки из левой таблицы, которым ничего не соответствует в правой.

---

# ⚙️ Дополнительное условие внутри `ON`

Условие соединения можно расширить:

```sql
SELECT *
FROM airplanes AS a
LEFT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
   AND s.fare_conditions = 'Business'
ORDER BY
    a.airplane_code ASC;
```

Здесь присоединяются только места класса:

```text
Business
```

Важно:

```sql
ON a.airplane_code = s.airplane_code
AND s.fare_conditions = 'Business'
```

условие относится к самому соединению таблиц.

---

# ⚠️ `ON` и `WHERE` — не одно и то же

Например:

```sql
LEFT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
   AND s.fare_conditions = 'Business'
```

сохраняет все строки из `airplanes`, даже если места `Business` не нашлись.

Если написать:

```sql
LEFT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
WHERE s.fare_conditions = 'Business'
```

то строки без найденного места будут отфильтрованы условием `WHERE`.

Для внешних соединений (`LEFT`, `RIGHT`, `FULL`) расположение условия может менять результат.

---

# 🔴 `RIGHT JOIN`

`RIGHT JOIN` сохраняет все строки из правой таблицы.

```sql
SELECT *
FROM airplanes AS a
RIGHT JOIN seats AS s
    ON a.airplane_code = s.airplane_code
WHERE a.airplane_code IS NULL;
```

Правая таблица:

```text
seats
```

Если строка из `seats` не нашла соответствия в `airplanes`, поля таблицы `airplanes` будут `NULL`.

Условие:

```sql
WHERE a.airplane_code IS NULL
```

позволяет найти строки справа без соответствия слева.

---

# 🟣 `FULL OUTER JOIN`

`FULL OUTER JOIN` сохраняет:

* совпавшие строки;
* строки только из левой таблицы;
* строки только из правой таблицы.

```sql
SELECT *
FROM airplanes AS a
FULL OUTER JOIN seats AS s
    ON a.airplane_code = s.airplane_code
WHERE a.airplane_code IS NULL;
```

---

# 🟣 `FULL JOIN`

Можно писать короче:

```sql
FULL JOIN
```

вместо:

```sql
FULL OUTER JOIN
```

Пример:

```sql
SELECT *
FROM airplanes AS a
FULL JOIN seats AS s
    ON a.airplane_code = s.airplane_code;
```

---

# 🧩 Главное отличие типов `JOIN`

```text
INNER JOIN
    → только совпавшие строки

LEFT JOIN
    → все строки слева + совпадения справа

RIGHT JOIN
    → все строки справа + совпадения слева

FULL JOIN
    → все строки из обеих таблиц

CROSS JOIN
    → каждая строка первой таблицы
      соединяется с каждой строкой второй
```

---

# ✖️ `CROSS JOIN`

`CROSS JOIN` создаёт все возможные комбинации строк.

На занятии использовали:

```sql
SELECT
    a.model,
    fc.fare_conditions
FROM airplanes AS a
CROSS JOIN (
    VALUES
        ('Economy'),
        ('Comfort'),
        ('Business')
) AS fc(fare_conditions);
```

Для каждого самолёта будут созданы варианты:

```text
Economy
Comfort
Business
```

Например, для одного самолёта:

```text
Boeing 737
```

получится:

```text
Boeing 737 | Economy
Boeing 737 | Comfort
Boeing 737 | Business
```

---

# 📦 `VALUES` как временный набор строк

В запросе:

```sql
VALUES
    ('Economy'),
    ('Comfort'),
    ('Business')
```

создаётся набор из трёх строк.

Затем ему задаётся псевдоним:

```sql
AS fc(fare_conditions)
```

Где:

```text
fc               → псевдоним набора
fare_conditions  → имя его столбца
```

После этого можно обращаться к нему:

```sql
fc.fare_conditions
```

---
