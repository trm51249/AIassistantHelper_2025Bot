import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Обработчики команд
def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение при команде /start."""
    user = update.effective_user
    update.message.reply_text(
        f'Привет, {user.first_name}! Я ваш AI-помощник для учёбы. Чем могу помочь?'
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Отправляет информацию о доступных командах."""
    update.message.reply_text('Доступные команды:\n'
                             '/start - начать общение с ботом\n'
                             '/help - показать справку')

def echo(update: Update, context: CallbackContext) -> None:
    """Обрабатывает сообщения пользователя."""
    update.message.reply_text(f"Вы написали: {update.message.text}")

def main() -> None:
    """Запускает бота."""
    # Создаем экземпляр Updater и передаем ему токен бота
    updater = Updater(BOT_TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик для сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
