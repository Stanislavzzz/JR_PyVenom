# Шпаргалка: PostgreSQL — поиск по строкам и строковые функции

# 🔎 Точное сравнение строк

## Найти аэропорты Москвы

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city = 'Moscow';
```

Условие:

```sql
city = 'Moscow'
```

означает: значение столбца `city` должно точно совпадать со строкой `'Moscow'`.

Важно:

```text
=      → точное совпадение
LIKE   → поиск по шаблону
ILIKE  → поиск по шаблону без учета регистра
```

---

# 🔍 Поиск по шаблону: `LIKE`

`LIKE` позволяет искать строки не по точному значению, а по шаблону.

В шаблонах используются специальные символы:

```text
%  → любое количество любых символов
_  → ровно один любой символ
```

---

## `%` — любое количество символов

### Строка начинается с `Mos`

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city LIKE 'Mos%';
```

Шаблон:

```text
Mos%
```

означает:

```text
строка начинается с Mos,
а после Mos может быть любое количество символов
```

Например:

```text
Moscow
```

подходит под этот шаблон.

---

## `_` — ровно один любой символ

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city LIKE 'Mos___';
```

Шаблон:

```text
Mos___
```

означает:

* строка начинается с `Mos`;
* после `Mos` должно быть ровно три любых символа.

Например:

```text
Moscow
```

подходит:

```text
Mos + cow
```

---

## Комбинация `_` и `%`

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city LIKE '_o%';
```

Шаблон:

```text
_o%
```

означает:

1. первый символ может быть любым;
2. второй символ должен быть `o`;
3. после него может находиться любое количество символов.

---

# 🔤 `LIKE` и регистр

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city LIKE 'm%';
```

В PostgreSQL `LIKE` учитывает регистр.

Поэтому:

```text
'Moscow'
```

и:

```text
'moscow'
```

для `LIKE` являются разными строками.

Запрос:

```sql
WHERE city LIKE 'm%'
```

не найдет `Moscow`, если значение начинается с заглавной `M`.

---

# 🔡 Поиск без учета регистра: `ILIKE`

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city ILIKE 'mo%';
```

`ILIKE` работает похожим образом на `LIKE`, но не учитывает регистр букв.

Поэтому шаблон:

```text
mo%
```

может найти:

```text
Moscow
moscow
MOSCOW
```

---

# 🚫 Отрицание: `NOT ILIKE`

```sql
SELECT
    airport_code,
    airport_name,
    city
FROM airports
WHERE city NOT ILIKE 'mo%';
```

Запрос выбирает строки, которые **не подходят** под шаблон:

```text
mo%
```

То есть исключает города, начинающиеся с `mo`, независимо от регистра.

---

# 🔽 Преобразование в нижний регистр: `LOWER`

```sql
SELECT
    airport_code,
    LOWER(airport_code) AS lower_code,
    airport_name,
    city
FROM airports;
```

Функция:

```sql
LOWER(airport_code)
```

переводит буквы в нижний регистр.

Например:

```text
SVO → svo
DME → dme
```

Исходное значение в таблице при этом не изменяется.

`AS lower_code` задает имя вычисляемому столбцу в результате запроса.

---

# 🔼 Преобразование в верхний регистр: `UPPER`

```sql
SELECT
    airport_code,
    airport_name,
    city,
    UPPER(city) AS upper_city,
    LENGTH(city) AS len_city
FROM airports;
```

Функция:

```sql
UPPER(city)
```

переводит строку в верхний регистр.

Например:

```text
Moscow → MOSCOW
```

Исходные данные в таблице не изменяются.

---

# 📏 Длина строки: `LENGTH`

```sql
SELECT
    airport_code,
    airport_name,
    city,
    UPPER(city) AS upper_city,
    LENGTH(city) AS len_city
FROM airports;
```

Функция:

```sql
LENGTH(city)
```

возвращает количество символов в строке.

Например:

```text
Moscow → 6
```

---

## Использование `LENGTH` в `WHERE`

Можно фильтровать строки по их длине:

```sql
SELECT
    airport_code,
    airport_name,
    city,
    UPPER(city) AS upper_city,
    LENGTH(city) AS len_city
FROM airports
WHERE LENGTH(city) > 20;
```

Условие:

```sql
LENGTH(city) > 20
```

оставляет только города, название которых содержит больше 20 символов.

---

# 🔁 Замена текста: `REPLACE`

```sql
SELECT
    airport_code,
    airport_name,
    city,
    REPLACE(city, ' ', '__') AS upper_city,
    LENGTH(city) AS len_city
FROM airports
WHERE LENGTH(city) > 20;
```

Функция:

```sql
REPLACE(city, ' ', '__')
```

означает:

```text
взять значение city
найти каждый пробел
заменить его на два символа _
```

Например:

```text
New York
```

превратится в:

```text
New__York
```

Общий вид:

```sql
REPLACE(строка, что_ищем, на_что_заменяем)
```

В исходном запросе результат назван:

```sql
AS upper_city
```

Это только псевдоним столбца. Сама функция `REPLACE` не переводит текст в верхний регистр.

---

# ✂️ Удаление пробелов по краям: `TRIM`

```sql
SELECT
    UPPER(TRIM('     Bob Name    ')) AS result;
```

Сначала выполняется:

```sql
TRIM('     Bob Name    ')
```

Результат:

```text
Bob Name
```

`TRIM` удаляет пробелы в начале и в конце строки.

Пробел между словами остается.

---

# 🔗 Вложенные функции

Функции можно вкладывать друг в друга:

```sql
UPPER(TRIM('     Bob Name    '))
```

Выполнение идет изнутри наружу.

Сначала:

```sql
TRIM('     Bob Name    ')
```

получаем:

```text
Bob Name
```

Затем:

```sql
UPPER('Bob Name')
```

получаем:

```text
BOB NAME
```

Полный запрос:

```sql
SELECT
    UPPER(TRIM('     Bob Name    ')) AS result;
```

---

# 🧩 `LIKE`, `%` и `_` — кратко

## Начинается с `Mos`

```sql
WHERE city LIKE 'Mos%'
```

Подходит:

```text
Moscow
```

---

## Начинается с `Mos` и после него ровно 3 символа

```sql
WHERE city LIKE 'Mos___'
```

Подходит:

```text
Moscow
```

---

## Второй символ — `o`

```sql
WHERE city LIKE '_o%'
```

Схема:

```text
любой символ + o + любое продолжение
```

---

## Начинается с `mo`, регистр не важен

```sql
WHERE city ILIKE 'mo%'
```

Подойдут, например:

```text
Moscow
moscow
MOSCOW
```

---

## Не начинается с `mo`, регистр не важен

```sql
WHERE city NOT ILIKE 'mo%'
```

---

# 🧭 Основные строковые функции занятия

```sql
LOWER(value)
```

Перевести строку в нижний регистр.

```sql
UPPER(value)
```

Перевести строку в верхний регистр.

```sql
LENGTH(value)
```

Получить количество символов.

```sql
REPLACE(value, 'что найти', 'на что заменить')
```

Заменить часть строки.

```sql
TRIM(value)
```

Удалить пробелы в начале и конце строки.

---

# 📌 Главное

```text
=            → точное сравнение

LIKE         → поиск строки по шаблону
ILIKE        → LIKE без учета регистра
NOT ILIKE    → строка не должна подходить под шаблон

%            → любое количество любых символов
_            → ровно один любой символ

LOWER()      → нижний регистр
UPPER()      → верхний регистр
LENGTH()     → количество символов
REPLACE()    → заменить часть строки
TRIM()       → убрать пробелы по краям

AS           → задать псевдоним столбцу

Функции можно вкладывать:
UPPER(TRIM(...))
```