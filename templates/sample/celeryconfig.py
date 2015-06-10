from datetime import timedelta
from kombu import Exchange, Queue

BROKER_BACKEND = "redis"
BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost/0"

CELERY_IGNORE_RESULT = False#required as False when using TaskSet.join()
CELERY_DISABLE_RATE_LIMITS = True
CELERYD_HIJACK_ROOT_LOGGER = False
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = CELERY_TASK_SERIALIZER
CELERY_ACCEPT_CONTENT = [CELERY_TASK_SERIALIZER,]

#CELERY_SEND_EVENTS = True
#CELERY_ACKS_LATE = False

CELERYD_CONCURRENCY = 2
CELERYD_PREFETCH_MULTIPLIER = 4

CELERYBEAT_SCHEDULE = {
#    'function-vanity-name': {
#        'task': 'module.tasks.function',
#        'schedule': timedelta(seconds=60),
#    },
}
