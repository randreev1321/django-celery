# project/tasks/sample_tasks.py

import time

from celery import shared_task


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 2)
    return True
