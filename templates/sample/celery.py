from __future__ import absolute_import

import os
from datetime import timedelta
from celery import Celery
from kombu import Exchange, Queue

"""
Configure the following:
- project: name of project, usually a module to identify namespace
- config_from_object: import path to celeryconfig.py
- CELERY_IMPORTS: import path to tasks.py
"""

project = 'project'

app = Celery(project)
app.config_from_object('celeryconfig'.format(project))
app.conf.update(
    CELERY_IMPORTS=("tasks".format(project),),
    NAME=project,
    CELERY_DEFAULT_QUEUE=project,
    CELERY_DEFAULT_EXCHANGE=project,
    CELERY_DEFAULT_ROUTING_KEY=project,
    CELERY_QUEUES=(
        Queue(project, Exchange(project), routing_key=project),
    ),
)

if os.environ.get('CELERY_EAGER'):
    app.conf.update(
        CELERY_ALWAYS_EAGER=True,
        CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
    )
