from celery import Celery
from celery.schedules import crontab
from tasks import my_function

# Initialize Celery
app = Celery('tasks', broker='redis://redis:6379/0')

# Define the periodic task
app.conf.beat_schedule = {
    'call-my-function-every-1-minute': {
        'task': 'tasks.my_function',
        'schedule': crontab(minute='*/1'),  # Every 1 minutes
    },
}

app.conf.timezone = 'UTC'
