# Library API

Асинхронное REST API для управления каталогом книг на **FastAPI** и **SQLAlchemy 2.0**.

## 📦 Стек технологий
* **FastAPI**
* **SQLAlchemy 2.0** (Asyncio, MappedAsDataclass)
* **Pydantic v2**
* **aiosqlite** (SQLite)

## 🛠 Запуск

1. Установка зависимостей:
```bash
pip install fastapi uvicorn sqlalchemy aiosqlite pydantic
```

2. Запуск сервера:
```bash
uvicorn main:app --reload
```
*База данных `library.db` создается автоматически при первом старте.*

## 🗺 API Эндпоинты (`/api/v1/books`)

| Метод | Эндпоинт | Статус | Описание |
| :--- | :--- | :--- | :--- |
| `POST` | `/` | 201 Created | Добавить книгу (от 11 страниц) |
| `GET` | `/` | 200 OK | Получить все книги |
| `GET` | `/{id}` | 200 OK / 404 | Получить книгу по ID |
| `PUT` | `/{id}` | 200 OK / 404 | Обновить книгу по ID |
| `DELETE` | `/{id}` | 204 No Content / 404 | Удалить книгу по ID |

* Swagger-документация: `http://127.0.0`

## 📂 Структура проекта
* `database.py` — Подключение к БД и сессии (`SessionDep`).
* `main.py` — Точка входа и инициализация таблиц.
* `models/books.py` — SQLAlchemy модель таблицы `books`.
* `schemas/books.py` — Pydantic схемы валидации.
* `repository.py` — Асинхронные CRUD операции.
* `routers/books.py` — Эндпоинты приложения.
