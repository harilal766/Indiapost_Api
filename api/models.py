import requests
from credentials import USERNAME,PASSWORD


class ApiBase:
    def __init__(self,username,password):
        # Credentials
        self.username = username
        self.password = password
        
        self.base_url = "https://test.cept.gov.in/beextcustomer/v1/access/"
        self.headers = {
            "accept" : "application/json",
            "Content-Type" : "application/json",
        }
        self.body = {
            "username": self.username,
            "password": self.password
        }
    
    def make_request(self,endpoint:str):
        response = requests.post(url = self.base_url + endpoint, headers = self.headers,json = self.body)        
        return response
    
class Authentication(ApiBase):
    def customer_login(self):
        auth_response = self.make_request(endpoint='login')
        return auth_response
        

class Tracking(Authentication):
    pass

