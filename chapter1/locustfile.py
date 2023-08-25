#------------------------------------------------------------------------------
# chapter1/locustfile.py
# /hello URI에 부하 워크로드 생성
#------------------------------------------------------------------------------

from locust import HttpUser, task
import warnings

warnings.filterwarnings("ignore")

class User(HttpUser):
    @task
    def index(self):
        self.client.get("/hello", verify=False)
