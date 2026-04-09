import logging
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, ContextTypes,
    CallbackQueryHandler
)
from config import TOKEN
from database import init_db

logging.basicConfig(level=logging.INFO)

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Это бот знакомств ❤️\nНапиши /register")

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users[update.effective_user.id] = {}
    await update.message.reply_text("Введи имя:")

async def browse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пока нет анкет 😢")

async def like(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Лайк отправлен ❤️")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("browse", browse))
    app.add_handler(CallbackQueryHandler(like, pattern="like_"))

    app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())
    main()
