# Шпаргалка: PostgreSQL / SQL — базовые SELECT-запросы

## 🔍 Информация о PostgreSQL и подключении

### Показать версию PostgreSQL

```sql
SELECT version();
```

Возвращает информацию об установленной версии PostgreSQL.

### Показать текущего пользователя

```sql
SELECT current_user;
```

Возвращает пользователя, под которым выполнено подключение к PostgreSQL.

### Показать текущую базу данных

```sql
SELECT current_database();
```

Возвращает имя базы данных, к которой выполнено текущее подключение.

---

# 📋 Получение данных: `SELECT`

## Вывести все столбцы таблицы

```sql
SELECT *
FROM airplanes;
```

Обозначения:

* `SELECT` — выбрать данные;
* `*` — выбрать все столбцы;
* `FROM airplanes` — получить данные из таблицы `airplanes`.

Еще пример:

```sql
SELECT *
FROM airports;
```

---

## Вывести только нужные столбцы

```sql
SELECT country, city
FROM airports;
```

Запрос возвращает только столбцы:

* `country`;
* `city`.

---

# 🏷️ Псевдонимы столбцов: `AS`

Можно изменить название столбца в результате запроса.

```sql
SELECT
    country AS "Страна",
    city AS "Город Аэропорта"
FROM airports;
```

`AS` задает временное имя столбца только для результата запроса.

Если в названии есть пробелы или нужен определенный регистр, имя можно заключить в двойные кавычки:

```sql
city AS "Город Аэропорта"
```

---

# 🧮 Вычисления в `SELECT`

В запросе можно выполнять арифметические операции.

```sql
SELECT
    model,
    range / 1000 AS range_1000,
    speed,
    speed * 2 AS speed_2
FROM airplanes;
```

Примеры:

```sql
range / 1000
```

делит значение `range` на `1000`.

```sql
speed * 2
```

умножает значение `speed` на `2`.

Результату вычисления можно дать имя через `AS`.

---

# 🔗 Объединение строк: `||`

В PostgreSQL оператор `||` объединяет строки.

```sql
SELECT airplane_code || ' -!- ' || model AS airplane
FROM airplanes;
```

Например, из значений:

```text
773
Boeing 777-300
```

может получиться строка:

```text
773 -!- Boeing 777-300
```

---

# 🔢 Ограничение количества строк: `LIMIT`

### Получить первые 10 строк

```sql
SELECT *
FROM airports
LIMIT 10;
```

`LIMIT 10` означает: вернуть не более `10` строк.

Можно использовать вместе с выбором отдельных столбцов:

```sql
SELECT
    country AS "Страна",
    city AS "Город Аэропорта"
FROM airports
LIMIT 10;
```

---

# ♻️ Удаление повторов: `DISTINCT`

### Получить список стран без повторений

```sql
SELECT DISTINCT country
FROM airports;
```

Без `DISTINCT`:

```sql
SELECT country
FROM airports;
```

одна и та же страна может встретиться много раз.

С `DISTINCT` повторяющиеся значения удаляются.

---

## `DISTINCT` для нескольких столбцов

```sql
SELECT DISTINCT country, city
FROM airports;
```

В этом случае уникальность определяется по сочетанию:

```text
country + city
```

То есть PostgreSQL убирает повторяющиеся пары значений.

---

# ↕️ Сортировка: `ORDER BY`

## По возрастанию: `ASC`

```sql
SELECT DISTINCT country, city
FROM airports
ORDER BY country ASC;
```

`ASC` — сортировка по возрастанию.

Для текста это обычно означает от `A` к `Z`.

---

## По убыванию: `DESC`

```sql
SELECT DISTINCT country, city
FROM airports
ORDER BY country DESC;
```

`DESC` — сортировка по убыванию.

Для текста это обычно означает от `Z` к `A`.

---

## Сортировка по нескольким столбцам

```sql
SELECT DISTINCT country, city
FROM airports
ORDER BY country DESC, city ASC;
```

Сначала результат сортируется:

1. по `country` — по убыванию;
2. внутри одинаковой страны по `city` — по возрастанию.

---

# 🔎 Фильтрация данных: `WHERE`

`WHERE` оставляет только строки, которые подходят под условие.

## Сравнение чисел

```sql
SELECT model, range
FROM airplanes
WHERE range > 10000;
```

Будут выбраны только самолеты, у которых `range` больше `10000`.

---

## Основные операции сравнения

```text
=   равно
!=  не равно
>   больше
<   меньше
>=  больше или равно
<=  меньше или равно
```

Пример:

```sql
SELECT flight_id, route_no, status
FROM flights
WHERE status = 'Delayed';
```

---

## Не равно: `!=`

```sql
SELECT flight_id, route_no, status
FROM flights
WHERE status != 'Delayed';
```

Запрос выбирает строки, где статус не равен `Delayed`.

---

# ➕ Логическое условие `AND`

`AND` требует, чтобы выполнялись оба условия.

```sql
SELECT *
FROM airports
WHERE airport_code NOT IN ('SVO', 'DME', 'VKO')
  AND city = 'Moscow';
```

Строка попадет в результат, только если:

1. код аэропорта не входит в указанный список;
2. город равен `Moscow`.

---

# 🔀 Логическое условие `OR`

`OR` требует выполнения хотя бы одного условия.

```sql
SELECT
    model,
    range,
    speed
FROM airplanes
WHERE range > 10000 OR speed > 900;
```

Строка попадет в результат, если:

* `range > 10000`;
* или `speed > 900`;
* или выполняются оба условия.

---

# 🚫 Логическое отрицание `NOT`

`NOT` меняет результат условия на противоположный.

```sql
SELECT flight_id, route_no, status
FROM flights
WHERE NOT status != 'Delayed';
```

В данном примере выбираются строки, для которых условие:

```sql
status != 'Delayed'
```

не выполняется.

---

# 📦 Проверка по списку: `IN`

Вместо нескольких условий с `OR` можно использовать `IN`.

Так:

```sql
SELECT flight_id, route_no, status
FROM flights
WHERE status = 'Delayed' OR status = 'Cancelled';
```

можно записать короче:

```sql
SELECT flight_id, route_no, status
FROM flights
WHERE status IN ('Delayed', 'Cancelled');
```

`IN` проверяет, входит ли значение в указанный список.

---

# 🚫 Проверка отсутствия в списке: `NOT IN`

```sql
SELECT *
FROM airports
WHERE airport_code NOT IN ('SVO', 'DME', 'VKO');
```

Запрос выбирает аэропорты, код которых не входит в список:

```text
SVO
DME
VKO
```

---

# 📏 Проверка диапазона: `BETWEEN`

### Значение находится в диапазоне

```sql
SELECT *
FROM bookings
WHERE total_amount BETWEEN 500000 AND 1000000;
```

`BETWEEN` включает обе границы диапазона.

То есть условие соответствует:

```sql
total_amount >= 500000
AND total_amount <= 1000000
```

---

# 🚫 Значение вне диапазона: `NOT BETWEEN`

```sql
SELECT *
FROM bookings
WHERE total_amount NOT BETWEEN 500000 AND 1000000;
```

Запрос выбирает строки, где `total_amount` находится вне диапазона от `500000` до `1000000`.

---

# 🏆 Сортировка + ограничение результата

### Получить 10 бронирований с наибольшей суммой

```sql
SELECT *
FROM bookings
WHERE total_amount > 500000
ORDER BY total_amount DESC
LIMIT 10;
```

Что происходит:

1. `FROM bookings` — берем данные из таблицы `bookings`;
2. `WHERE total_amount > 500000` — оставляем бронирования дороже `500000`;
3. `ORDER BY total_amount DESC` — сортируем сумму от большей к меньшей;
4. `LIMIT 10` — оставляем первые `10` строк.

---

# 🧭 Общая структура изученного запроса

```sql
SELECT столбцы
FROM таблица
WHERE условие
ORDER BY столбец ASC
LIMIT количество;
```

Не все части обязательны.

Например:

```sql
SELECT model, range
FROM airplanes;
```

или:

```sql
SELECT *
FROM bookings
WHERE total_amount > 500000
ORDER BY total_amount DESC
LIMIT 10;
```

---

## 📌 Главное

```text
SELECT      → какие данные получить
FROM        → из какой таблицы
DISTINCT    → убрать повторяющиеся строки
AS          → дать столбцу временное имя
WHERE       → отфильтровать строки
AND         → должны выполняться оба условия
OR          → достаточно одного условия
NOT         → отрицание условия
IN          → значение входит в список
NOT IN      → значение не входит в список
BETWEEN     → значение находится в диапазоне
NOT BETWEEN → значение находится вне диапазона
ORDER BY    → отсортировать результат
ASC         → по возрастанию
DESC        → по убыванию
LIMIT       → ограничить количество строк
||          → объединить строки
```
