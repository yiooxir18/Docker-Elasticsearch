# Elasticsearch Search Engine

Проект поисковика на базе Elasticsearch предназначен для индексации и поиска текстовых документов (например, статей блога) с использованием Elasticsearch.

## Особенности

- Возможность индексировать текстовые файлы в Elasticsearch.
- Поиск по индексированным документам с использованием фразы или ключевых слов.

## Требования

- Docker и Docker Compose (для запуска Elasticsearch в контейнере).
- Python 3.7 или выше.
- Elasticsearch Python Client (`elasticsearch` пакет).

## Установка

### Запуск Elasticsearch с помощью Docker Compose

1. Установите Docker и Docker Compose на вашу систему.
2. Создайте файл `docker-compose.yml` с содержимым, указанным в предыдущих ответах.
3. Запустите Docker Compose:

   
```bash
docker-compose up -d
  ``` 

### Установка Elasticsearch Python Client

Установите необходимый пакет клиента Elasticsearch для Python:

bash
pip install elasticsearch==7.12.1

## Использование

Проект включает Python скрипт `search_engine.py`, который работает в двух режимах: запись и чтение.

### Режим записи

Чтобы проиндексировать текстовый файл, выполните команду:

```bash
python searchengine.py write <путькфайлу.txt>
```

### Режим чтения

Чтобы выполнить поиск по фразе, используйте команду:

```bash
python searchengine.py read "фраза для поиска"
```

## Настройка

Вы можете настроить параметры подключения к Elasticsearch в скрипте `search_engine.py`, если ваша конфигурация отличается от стандартной.

## Примеры

Создайте текстовый файл с именем `example.txt` и добавьте в него текст для индексации. Затем индексируйте его:

```bash
python searchengine.py write example.txt
```

После индексации выполните поиск:

```bash
python searchengine.py read "Programming"
```
