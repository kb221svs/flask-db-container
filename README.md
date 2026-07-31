# 🐳 Containerized Flask REST API with PostgreSQL

Простий та функціональний REST API сервіс на **Flask**, розгорнутий у контейнеризованому середовищі **Docker** із підключенням до бази даних **PostgreSQL**.

---

## 🛠️ Функціонал API

* `GET /` — Вітальне повідомлення.
* `GET /users` — Отримання списку всіх користувачів із БД.
* `POST /users` — Додавання нового користувача (`{"name": "Vika"}`).
* `DELETE /users/<id>` — Видалення користувача за його ID.

---

## 🧰 Стек технологій

* **Python 3** (Flask, `psycopg2-binary`)
* **PostgreSQL** (як СУБД)
* **Docker & Docker Compose** (для оркестрації сервісів)

---

## 🚀 Як запустити проєкт

1. Клонувати репозиторій
```bash
git clone [https://github.com/kb221svs/flask-docker-postgres.git](https://github.com/kb221svs/flask-docker-postgres.git)
cd flask-docker-postgres
2. Запустити через Docker Compose
Bash
docker-compose up --build -d
Після запуску сервіс буде доступний за адресою: http://localhost:5000

3. Зупинити контейнери
Bash
docker-compose down
