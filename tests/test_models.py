from tests.test_credentials import USERNAME, PASSWORD
from api.models import ApiBase
import re


class TestApiBase:
    instance = ApiBase(
        username=USERNAME, password=PASSWORD
    )
    assert re.match(r'\d{10}',instance.username)
    