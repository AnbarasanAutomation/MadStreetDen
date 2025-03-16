from locust import User, task, constant
from datetime import datetime


class LoadTest(User):
    wait_time = constant(1)
    @task
    def launch(self):
        print("launching the URL")

    @task
    def search(self):
        print(datetime.now())



