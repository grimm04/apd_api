from .base import *
from .env import *
 

ALLOWED_HOSTS = ['localhost','127.0.0.1'] 

DEBUG = True 
DATABASES = {
    'default': {
        'ENGINE': get_env_value('DATABASE_ENGINE'),
        'NAME': get_env_value('DATABASE_NAME'),
        'USER': get_env_value('DATABASE_USER'),
        'PASSWORD': get_env_value('DATABASE_PASS'),
        'HOST': get_env_value('DATABASE_HOST'),
        'PORT': get_env_value('DATABASE_PORT'),
        'OPTIONS': { 
            'driver': get_env_value('DATABASE_DRIVER'),
            'extra_params': get_env_value('DATABASE_EXTRA_PARAMS')
        },
        'TIME_ZONE': 'Asia/Jakarta'
    },
}