from .base import *
from cassandra import ConsistencyLevel
from cassandra.auth import PlainTextAuthProvider

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']

DATABASES.update({
    'cassandra': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': os.getenv('ASTRA_KEYSPACE'),
        'USER': os.getenv('ASTRA_DB_USERNAME'),
        'PASSWORD': os.getenv('ASTRA_DB_PASSWORD'),
        'OPTIONS': {
            'connection': {
                'cloud':{
                    'secure_connect_bundle': BASE_DIR / 'astra/astra-bundle.zip',
                },
                'auth_provider': PlainTextAuthProvider(username=os.getenv('ASTRA_DB_USERNAME'), password=os.getenv('ASTRA_DB_PASSWORD'))
            },
        }
    }
})
