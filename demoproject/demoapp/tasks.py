# Create your tasks here

from celery.decorators import task

@task(name="add")
def add(x=1, y=1000):
    return x + y
