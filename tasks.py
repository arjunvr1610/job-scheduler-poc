from celery import Celery

# Initialize Celery
app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def my_function():
    print("Function is called every 1 minutes")