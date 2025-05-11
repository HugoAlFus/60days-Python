from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    await update.message.reply_text(
        f"¡Hola {user_first_name}! 👋 Bienvenido al bot de prueba de 60DaysOfPython. Este bot pertenece al día 26 el "
        f"reto.")
