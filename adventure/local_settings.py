DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'adventure',
        'USER': 'postgres',
        'PASSWORD': 'hakunamatata',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#ssl
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
