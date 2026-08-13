import json

with open("credentials.json", "r") as json_file:
    creds_data = json.load(json_file)
    
    USERNAME = creds_data["username"]
    PASSWORD = creds_data["password"]