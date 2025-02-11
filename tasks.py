from celery import Celery

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6380/0')

@app.task
def my_function():
    print("Function is called every 1 minutes")