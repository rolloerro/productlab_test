🧠 ProductLab Test Project

Demo-проект на FastAPI + aiogram
Тестовое задание для ProductLab.pro — демонстрация развёртывания Telegram-бота и REST API на FastAPI.

🚀 О проекте

Проект создан для демонстрации навыков интеграции FastAPI (backend API) и aiogram (Telegram-бот) в одном приложении.
Локальный сервер пробрасывается наружу через ngrok — это позволяет показать работу API и Swagger-документации без деплоя на VPS.

Бот и сервер работают асинхронно в одном event loop, обрабатывая запросы независимо.

⚙️ Технологии
Компонент	Описание
🐍 Python 3.12+	Язык проекта
⚡ FastAPI	Backend + Swagger
🤖 aiogram	Telegram-бот
🌍 ngrok	Внешний доступ
🔐 dotenv	Безопасное хранение токенов
🧱 Uvicorn	ASGI-сервер
🧩 Установка и запуск
git clone https://github.com/rolloerro/productlab_test.git
cd productlab_test
python -m venv venv
source venv/bin/activate   # macOS / Linux
# или
venv\Scripts\activate      # Windows
pip install -r requirements.txt


Создай файл .env в корне проекта и добавь токен Telegram-бота:

BOT_TOKEN=your_telegram_token_here


Запусти сервер и бота:

python main.py


Swagger будет доступен по адресу:

http://localhost:8080/docs


Для внешнего доступа через ngrok:

ngrok http 8080

⚙️ Функционал
Компонент	Описание
/	Корневой эндпоинт API
/health	Проверка статуса сервера
/docs	Swagger-документация
/start (в Telegram)	Приветствие от бота
🧠 Пример результата
Swagger: https://fay-spleeniest-arvilla.ngrok-free.dev/docs
Bot: @productlab01_bot

🧩 Архитектура
main.py
 ├── FastAPI server (порт 8080)
 │    ├── /health
 │    └── /docs
 └── aiogram Bot (Telegram)
      └── /start handler


Бот и сервер работают в отдельных асинхронных потоках, что позволяет сохранять отзывчивость и стабильность.

🪄 Автор

Владимир Копылов
🧠 Fullstack / AI & ML Engineer | Product Innovator | MedTech Integrator
📍 Москва | 🌍 Удалённо / гибрид
📧 coplow@yandex.ru

💬 Telegram: @MSL72Rph

💻 GitHub: rolloerro

🎯 Миссия

Создаю умные системы, где код и медицина соединяются в пользу людей.
Product + AI + Data = результат, который работает в жизни, а не только на бумаге.
