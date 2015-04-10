# -*- coding:utf-8 -*-
# PROJECT_NAME : django-super-cache
# FILE_NAME    : 
# AUTHOR       : younger shen
from .exceptions import CacheMissingError


class BaseBackend(object):
    name_ = 'backend'

    def __init__(self, settings):
        self.settings = settings

    def set(self, content, key):
        pass

    def get(self, key):
        pass


class FileBackend(BaseBackend):
    name = 'file'

    def __init__(self, settings):
        self.settings = settings
        self.cache_dir = settings.get('file_dir')

    def set(self, content, key):
        cache_file = self.cache_dir + key

        with open(cache_file, 'w') as f:
            f.write(content)
            f.flush()

    def get(self, key):
        cache_file = self.cache_dir + key

        try:
            with open(cache_file, 'r') as f:
                return f.read()
        except IOError:
            raise CacheMissingError(key=key)
