from tests.test_credentials import USERNAME, PASSWORD
from api.models import ApiBase
import re


class TestApiBase:
    instance = ApiBase(
        username=USERNAME, password=PASSWORD
    )
    
    def test_username(self):
        username_check = re.fullmatch(r'\d{10}',self.instance.username)
        assert username_check
        assert self.instance.password == PASSWORD


    def test_make_request(self):
        resp = self.instance.make_request(endpoint = 'login')
        assert resp
