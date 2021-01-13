from .base import *
from cassandra import ConsistencyLevel

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']

DATABASES.update({
    'cassandra': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': os.getenv('CASSANDRA_KEYSPACE'),
        'USER': os.getenv('CASSANDRA_DB_USERNAME'),
        'PASSWORD': os.getenv('CASSANDRA_DB_PASSWORD'),
        'HOST': '172.18.0.2',
        'OPTIONS': {
            'replication': {
                'strategy_class': 'SimpleStrategy',
                'replication_factor': 2
            },
            'connection': {
                'consistency': ConsistencyLevel.ONE,
                'retry_connect': True
            },
            'session': {
                'default_timeout': 10,
                'default_fetch_size': 10000
            }
        }
    }
})

SITE_ID = 1
CASSANDRA_FALLBACK_ORDER_BY_PYTHON = True