import os
from celery import Celery
from celery.schedules import crontab
from NewsPaper.tasks import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')
app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday': {
        'task': 'NewsPaper.tasks.my_job',
        'schedule': 30
        # 'schedule': crontab(hour=9, minute=0, day_of_week=1),
    },
}

send_mail.delay()
