from celery import shared_task
import time


@shared_task
def send_mail():
    for x in range(5):
        print(x)
        time.sleep(1)
