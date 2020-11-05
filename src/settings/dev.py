from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c+y4yap017brcmccwj4a4!+2p8bj%6=uc7$v5%zn8m$a031t6o'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
