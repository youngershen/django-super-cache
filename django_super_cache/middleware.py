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
backend = get_backend(settings)


class SuperCacheMiddleware(object):

    @staticmethod
    def process_response(request, response):
        cache_key = get_cache_key(request)
        content = response.content
        if getattr(request, 'cache', None):
            backend.set(content, cache_key)

        return response

    @staticmethod
    def process_request(request):
        method = request.method

        if method != 'GET':
            return

        cache_key = get_cache_key(request)
        try:
            cache = backend.get(cache_key)
        except CacheMissingError:
            setattr(request, 'cache', True)
            return
        else:
            return HttpResponse(cache)