Установка и запуск
Клонируй репозиторий:

bash
Copy
Edit
git clone https://github.com/newbshark/drum_motivation_bot.git
cd drum_motivation_bot
Создай и активируй виртуальное окружение (рекомендуется):

bash
Copy
Edit
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
Установи зависимости:

bash
Copy
Edit
pip install -r requirements.txt
Создай файл .env в корне проекта и пропиши туда:

ini
Copy
Edit
API_ID=твой_api_id
API_HASH=твой_api_hash
BOT_TOKEN=токен_бота_из_@BotFather
CHANNEL_ID=-100номер_канала
Запусти бота:

bash
Copy
Edit
python bot.py
Файлы проекта
auth_test.py — тест авторизации через Pyrogram

read_channel.py — скрипт для поиска сообщений в канале по ключевому слову

bot.py — основной файл с логикой Telegram-бота

.env — файл с секретами и настройками (НЕ кладём в git)

Как использовать
Запусти bot.py — бот стартует и ждёт сообщений

Отправь боту слово-пароль (например, коммьюнити)

Бот ищет сообщения с этим словом в описании уроков в канале

Выбираешь кнопку с нужным уроком — бот пересылает видео и текст урока тебе в чат

Цель проекта
Создать удобный и простой инструмент для учеников барабанов, который помогает быстро получать уроки без сложных настроек, повышая мотивацию и вовлечённость в обучение.

Контакты
Автор: Вадим Васильев (@mrvasilievv)
GitHub: newbshark

