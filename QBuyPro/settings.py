
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '_-%ej4#&12+t7oy7ngk80pf%r7_v&vb=f4d%$&-v#(g7h-7y+n'

DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userapp',
    'order',
    'actives',
    'goods'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QBuyPro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'QBuyPro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
     'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'xq2',
        "HOST": 'xm.imzhangao.com',
        "PORT": 3306,
        "USER": 'root',
        "PASSWORD": '19960207',
        "CHARSET" : 'utf-8'

    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/m/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 配置缓存Cache
CACHES = {
    'default': {
        "BACKEND": 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://xm.imzhangao.com:6379/6',
        # "TIMEOUT": 300,
        # 'OPTIONS': {
        #     'MAX_ENTRIES': 300,
        #     'CULL_FREQUENCY': 3
        }
    }

#     'html': {
# "BACKEND": 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': 'unique-snowflake',
#     },
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://xm.imzhangao.com:6379/6',
#         "OPTIONS": {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'SOCKET_CONNECT_TIMEOUT': 10,
#             'SOCKET_TIMEOUT': 10
#         }
#     }
# }


# 配置SESSION
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_NAME = 'SESSION_ID'
# SESSION_COOKIE_PATH = '/'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 604800  # 有效时间两周


# 配置日志
# 配置日志
LOGGING = {
    'version': 1.0,
# 定义日志的格式，可以定义多个
    'formatters':{
        'simple': {
            'format': '[%(asctime)s %(name)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
# 定义日志的处理方式，里面的名字可以自定义，设置每一个的处理级别和方式
    'handlers': {
        'out': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'filename': 'qbuy.log'
        },
    },
# 使用日志，选择处理方式从刚才自己定义的处理方式中，设置级别
    'loggers': {
        'django': {
            'handlers': ['out', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'qbuy': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# 配置Celery
CELERY_IMPORTS = ('')
