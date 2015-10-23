from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def counter():
    return 0;
