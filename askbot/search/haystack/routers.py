from django.utils.translation import get_language
from django.conf import settings

from haystack.routers import BaseRouter
from haystack.constants import DEFAULT_ALIAS

class LanguageRouter(BaseRouter):

    def for_read(self, **hints):
        if getattr(settings, 'ASKBOT_MULTILINGUAL'):
            return 'default_' + get_language()
        else:
            return DEFAULT_ALIAS

    def for_write(self, **hints):
        if getattr(settings, 'ASKBOT_MULTILINGUAL'):
            return 'default_' + get_language()
        else:
            return DEFAULT_ALIAS
