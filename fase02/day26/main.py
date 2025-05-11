import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start import start
from handlers.help import help_command
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

# Añadir manejadores
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

# Ejecutar el bot
if __name__ == "__main__":
    print("Bot iniciado...")
    app.run_polling()
