from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = Celery('api', backend='amqp', broker='amqp://%s:%s@%s/%s' % (settings.MQ_USER, settings.MQ_PASSWORD, settings.MQ_HOST, settings.MQ_VHOST))
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
