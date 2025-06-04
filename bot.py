import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
from read_channel import find_messages_by_keyword  # подключаем функцию

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # пример: -1001234567890

# Храним данные временно в памяти
user_keywords = {}
user_results = {}

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Напиши своё слово-мотивацию, и я найду уроки, которые тебе подойдут."
    )

# Обработка текстового сообщения — это слово-пароль
async def handle_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    keyword = update.message.text.strip().lower()
    user_keywords[user_id] = keyword

    await update.message.reply_text(f"🔍 Ищу уроки с ключевым словом: «{keyword}»...")

    # Ищем уроки
    messages = await find_messages_by_keyword(keyword)

    if not messages:
        await update.message.reply_text("😔 Уроков с таким словом не найдено.")
        return

    user_results[user_id] = messages

    # Создаём кнопки
    keyboard = []
    for i, msg in enumerate(messages):
        label = msg["text"][:30] + "..." if msg["text"] else "Урок без текста"
        keyboard.append([InlineKeyboardButton(f"{i + 1}. {label}", callback_data=str(i))])

    await update.message.reply_text(
        "🎓 Найдены уроки. Нажми, чтобы получить:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Обработка выбора урока по кнопке
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if user_id not in user_results:
        await query.edit_message_text("Сначала отправь своё мотивационное слово.")
        return

    idx = int(query.data)
    messages = user_results[user_id]

    if idx >= len(messages):
        await query.edit_message_text("Неверный выбор.")
        return

    message_id = messages[idx]["message_id"]

    # Пересылаем сообщение из канала
    await context.bot.forward_message(
        chat_id=user_id,
        from_chat_id=CHANNEL_ID,
        message_id=message_id,
    )

    await query.edit_message_text("📦 Урок отправлен!")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Просто пришли слово и получи уроки 🔑")

# Запуск бота
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_keyword))
    app.add_handler(CallbackQueryHandler(handle_button))

    print("🤖 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
