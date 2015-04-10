# -*- coding:utf-8 -*-
# PROJECT_NAME : django-super-cache
# FILE_NAME    : 
# AUTHOR       : younger shen
import hashlib
from django.conf import settings
from .settings import DJANGO_SUPER_CACHE_ENABLED
from .settings import DJANGO_SUPER_CACHE_BACKEND
from .settings import DJANGO_SUPER_CACHE_EXPIRE_TIME
from .settings import DJANGO_SUPER_CACHE_AUTO_UPDATE
from .settings import DJANGO_SUPER_CACHE_FILE_DIR
from .backends import FileBackend
from .exceptions import BackendNotFoundError

def get_settings():
    enabled = getattr(settings, 'DJANGO_SUPER_CACHE_ENABLED', None)
    backend = getattr(settings, 'DJANGO_SUPER_CACHE_BACKEND', None)
    expire_time = getattr(settings, 'DJANGO_SUPER_CACHE_EXPIRE_TIME', None)
    auto_update = getattr(settings, 'DJANGO_SUPER_CACHE_AUTO_UPDATE', None)
    file_dir = getattr(settings, 'DJANGO_SUPER_CACHE_FILE_DIR', None)

    if not enabled:
        enabled = DJANGO_SUPER_CACHE_ENABLED

    if not backend:
        backend = DJANGO_SUPER_CACHE_BACKEND

    if not expire_time:
        expire_time = DJANGO_SUPER_CACHE_EXPIRE_TIME

    if not auto_update:
        auto_update = DJANGO_SUPER_CACHE_AUTO_UPDATE

    if not file_dir:
        file_dir = DJANGO_SUPER_CACHE_FILE_DIR

    return dict(enabled=enabled, backend=backend, expire_time=expire_time, auto_update=auto_update, file_dir=file_dir)


def get_cache_key(request):
    path_info = request.META.get('PATH_INFO')
    query_string = request.META.get('QUERY_STRING')
    page_key = path_info + '?' + query_string
    md5 = hashlib.md5(page_key)
    return md5.hexdigest()


def get_backend(cache_settings):
    backend = cache_settings.get('backend', None)
    if backend == 'file':
        return FileBackend(settings)

    raise BackendNotFoundError(name=backend)