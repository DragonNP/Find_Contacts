import config
import logging
import sys
from telegram.ext import Updater

updater = None
logger = logging.getLogger('bot')

if config.MODE == "dev":
    def run(updater):
        updater.start_polling()
elif config.MODE == "prod":
    def run(updater):
        updater.start_webhook(listen="0.0.0.0", port=config.PORT, url_path=config.TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(config.HEROKU_APP_NAME, config.TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def send_message(chat_id, text, reply_markup=None):
    logger.info('send msg to ' + chat_id)
    sendMessage(chat_id=chat_id, text=text, reply_markup=reply_markup)


def add_handlers(handlers):
    if type(handlers) != list:
        logger.debug('add handler')
        updater.dispatcher.add_handler(handlers)
        return

    logger.debug('add handlers')
    for handler in handlers:
        updater.dispatcher.add_handler(handler)


def add_error_handlers(handlers):

    if type(handlers) != dict:
        logger.debug('add error handler')
        updater.dispatcher.add_error_handler(handlers)
        return

    logger.debug('add error handlers')
    for handler in handlers:
        updater.dispatcher.add_error_handler(handler)


def start():
    global updater

    logger.info("Starting bot")
    if config.MODE == 'dev':
        updater = Updater(config.TOKEN, request_kwargs=config.REQUEST_KWARGS, use_context=True)
    else:
        updater = Updater(config.TOKEN, use_context=True)

    run(updater)
