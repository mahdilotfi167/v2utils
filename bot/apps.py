from django.apps import AppConfig
from django.conf import settings
import os


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
