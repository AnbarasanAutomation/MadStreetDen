from locust import User, task
from datetime import datetime


class LoadTest(User):

    @task
    def launch(self):
        print("launching the URL")

    @task
    def search(self):
        print(datetime.now())



