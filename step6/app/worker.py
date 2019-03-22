import os

from celery import Celery
from redis import Redis

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379'),
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND',
    'redis://redis:6379',
)

celery = Celery(
    'worker',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
)
redis = Redis(host='redis', port=6379)


@celery.task
def add_to_hits(x=1):
    return redis.incr('hits', x)
