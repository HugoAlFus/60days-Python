from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "ℹ️ *Ayuda del Bot*\n\n"
        "/start - Inicia el bot y da la bienvenida.\n"
        "/help - Muestra este mensaje de ayuda.\n"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")
