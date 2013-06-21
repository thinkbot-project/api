from .base import *

BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_USER = "ubuntu"
BROKER_PASSWORD = "somepassword"
BROKER_VHOST = "thinkbot_vhost"

CELERY_BACKEND = "amqp"
CELERY_RESULT_DBURI = ""
