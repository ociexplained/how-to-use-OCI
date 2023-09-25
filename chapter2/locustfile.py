#------------------------------------------------------------------------------
# chapter2/locustfile.py
# /hello URI에 부하 워크로드 생성
#------------------------------------------------------------------------------

from locust import HttpUser, task

class Book(HttpUser):
    @task
    def hello(self):
        # /vi/book/hello API를 호출
        self.client.get("/v1/book/hello")
