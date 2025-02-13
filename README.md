# Django Marketplace API

## 📌 Описание
Этот проект — API для маркетплейса, построенный на Django и Django REST Framework. 
Он включает поддержку WebSocket через Django Channels и использует PostgreSQL в качестве базы данных.

## 🚀 Технологии
- **Django** — основной фреймворк
- **Django REST Framework** — для создания API
- **Django Channels** — поддержка WebSocket
- **PostgreSQL** — основная база данных
- **Redis** — для WebSocket каналов
- **drf-spectacular / drf-yasg** — для генерации документации

## 📂 Установка и запуск
### 1. Клонируйте репозиторий
```bash
 git clone https://github.com/your-username/your-repo.git
 cd your-repo
```

### 2. Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate  # Windows
```

### 3. Установите зависимости
В проекте есть файл `requirements.txt`, который содержит все необходимые зависимости. Установите их с помощью команды:
```bash
pip install -r requirements.txt
```

### 4. Настройте переменные окружения
Создайте файл `.env` в корневой директории и укажите переменные:
```ini
SECRET_KEY=your-secret-key
DB_NAME=marketplace_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Запустите миграции
```bash
python manage.py migrate
```

### 6. Создайте суперпользователя (необязательно)
```bash
python manage.py createsuperuser
```

### 7. Запустите сервер разработки
```bash
python manage.py runserver
```
Сервер будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔗 WebSocket
WebSocket подключается через Redis. Чтобы запустить его локально, установите Redis и запустите сервер.
```bash
redis-server
```
После этого можно использовать WebSocket через `channels`.

## 📜 Документация API
Генерируется автоматически с помощью **drf-spectacular** и **drf-yasg**.
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## 📌 Автор
**Жанылмырза** — [GitHub](https://github.com/Zhanylmyrza)

