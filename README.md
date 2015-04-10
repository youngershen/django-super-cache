#django-super-cache


a single page cache for django, easy to use, but now it is not much powerful, there is only one backend to use , is file backend.


usage:
    put django_super_cache in your INSTALLED_APPS

    in settings.py

    DJANGO_SUPER_CACHE_ENABLED = False

    DJANGO_SUPER_CACHE_BACKEND = 'file'

    DJANGO_SUPER_CACHE_EXPIRE_TIME = 24

    DJANGO_SUPER_CACHE_AUTO_UPDATE = True

    DJANGO_SUPER_CACHE_FILE_DIR = '/var/cache/'


there is only one backend now, you only can use file backend , and will improve sooner.