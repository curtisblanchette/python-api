from locust import HttpUser, between, task

import random


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.client.post("/expenses", {
            "description": "salary",
            "amount": 25123
        })

    @task
    def get_requests(self):
        self.client.get("/expenses")
        self.client.get("/incomes")

    @task
    def homepage(self):
        self.client.get('/')

    @task
    def post_requests(self):
        self.client.post("/expenses", {
            "description": "salary",
            "amount": random.randint(300, 1000)
        })