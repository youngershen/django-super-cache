# -*- coding:utf-8 -*-
# PROJECT_NAME : django-super-cache
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.utils.encoding import python_2_unicode_compatible
from .messages import CACHE_MISSING_ERROR_MSG
from .messages import BACKND_NOT_FOUND_ERROR_MSG


@python_2_unicode_compatible
class CacheMissingError(Exception):

    def __init__(self, key=None):
        self.message = CACHE_MISSING_ERROR_MSG.format(key=key) if key else CACHE_MISSING_ERROR_MSG

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class BackendNotFoundError(Exception):

    def __init__(self, name=None):
        self.message = BACKND_NOT_FOUND_ERROR_MSG.format(name=name) if name else CACHE_MISSING_ERROR_MSG

    def __str__(self):
        return self.message