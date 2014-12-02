# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

# based on 12factor, enviroment variable will take the higher priority
#For database settings, the environment value with key "DATABASE_URL" will override all the settings.

#MYSQL
# the format for url: mysql://USERNAME:PASSWORD@HOST:PORT/DB_NAME
# the default:
# HOST: localhost
# PORT: 3306
# USER: intros
# PASSWORD: intros
# DB: intros
# Uncomment this line for override the setings with mysql.
#DATABASES = {'default': dj_database_url.config(default='mysql://intros:intros@localhost:3306/intros')}

#POSTGRES
# the format for url: postgres://USERNAME:PASSWORD@HOST:PORT/DB_NAME
# the default:
# HOST: localhost
# PORT: 5432
# USER: intros
# PASSWORD: intros
# DB: intros
# Uncomment this line for override the setings with mysql.
#DATABASES = {'default': dj_database_url.config(default='postgres://intros:intros@localhost:5432/intros')}


#add key based on https://developers.google.com/api-client-library/python/guide/aaa_oauth
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://mail.google.com']

try:
    from .local import *
except ImportError:
    pass
