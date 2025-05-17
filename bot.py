import logging
from telegram.ext import Updater, CommandHandler

# Configuração de logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Comando /start
def start(update, context):
    update.message.reply_text('Bot R.N.F. ativado com sucesso!')

# Comando /status
def status(update, context):
    update.message.reply_text('Sistema R.N.F. está operacional, comandante!')

def main():
    # Insira o seu token aqui
    updater = Updater("SEU_TOKEN_AQUI", use_context=True)
    dp = updater.dispatcher

    # Comandos registrados
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("status", status))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
