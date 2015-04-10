# -*- coding:utf-8 -*-
# PROJECT_NAME : django-super-cache
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.http import HttpResponse
from .utils import get_settings
from .utils import get_cache_key
from .utils import get_backend
from .exceptions import CacheMissingError
settings = get_settings()
backend = get_backend(settings.get('backend', None))


class SuperCacheMiddleware(object):

    @staticmethod
    def process_response(request, response):
        return response

    @staticmethod
    def process_request(request):
        cache_key = get_cache_key(request)
        try:
            cache = backend.get(cache_key)
        except CacheMissingError:
            pass
        else:
            return HttpResponse(cache)