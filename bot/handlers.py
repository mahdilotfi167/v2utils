import threading
import telebot
import logging
from telebot import types


telebot.apihelper.ENABLE_MIDDLEWARE = True

logger = logging.getLogger(__name__)


class Bot:
    user_query = None
    
    def wrap_handler(self, func):
        def wrapper(message):
            res = func(message)
            self.send(message, res)
        return wrapper
    
    def send(self, message, object):
        if object is None:
            return
        if type(object) == str:
            self._bot.send_message(message.chat.id, object)
        elif type(object) == types.InputFile:
            self._bot.send_document(message.chat.id, object)
        elif hasattr(object, '__iter__'):
            for item in object:
                self.send(message, item)
        else:
            raise TypeError('Unsupported type')
    
    def __init__(self, token):
        self._bot = telebot.TeleBot(token, parse_mode=None)
        self._thread = None
        for field in dir(self):
            if field.startswith('handle_'):
                self._bot.register_message_handler(self.wrap_handler(getattr(self, field)), commands=[field.removeprefix('handle_')])
            if field.endswith('_middleware'):
                self._bot.register_middleware_handler(getattr(self, field))

    def user_middleware(self, _, update):
        username = update.message.from_user.username
        if self.user_query:
            update.message.user = self.user_query.filter(username=username).first()

    def run_polling(self):
        self._thread = threading.Thread(target=self._bot.infinity_polling)
        self._thread.setDaemon(True)
        self._thread.start()
        logger.warning('Bot started')
        
    def handle_auth_error(self, message):
        return None
        
    def close(self):
        if self._thread:
            self._thread.join()
