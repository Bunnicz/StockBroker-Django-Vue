import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "get_world_stock_data_every_5_sec": {
        "task": "broker.tasks.get_world_stock_from_stooq_pl",
        "schedule": 5,
        # "args": (16, 16),
    },
    # "add_values_every_5_sec": {
    #     "task": "broker.tasks.add",
    #     "schedule": 5,
    #     "args": (16, 16),
    # },
}
app.conf.timezone = 'UTC'
