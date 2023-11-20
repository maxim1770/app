from datetime import timedelta

from celery import Celery

from app.core.config import settings

# celery = Celery('celery', broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0')
celery = Celery('celery', broker=f'redis://localhost:{settings.REDIS_PORT}/0')



celery.conf.beat_schedule = {
    'post-every-day': {
        'task': 'celery.post_to_tg',
        # 'schedule': crontab(minute=0, hour='*/24'),  # Расписание выполнения задачи, например, каждые 4 часа
        'schedule': timedelta(minutes=1),
    },
}

if __name__ == '__main__':
    celery.start()
