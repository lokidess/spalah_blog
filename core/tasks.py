import time

from blog import celery_app


@celery_app.task
def test_task():
    time.sleep(3)
    print("Hello")
