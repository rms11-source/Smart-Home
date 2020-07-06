import requests
import json

# api-endpoint 
URL_GET = "http://192.168.1.102:5000//last-sensors-data-aggregated"
URL_POST = "http://192.168.1.102:5000//health_state"
  
def get_data():
    print("Getting data from the server")
    r = requests.get(url = URL_GET) 
    status = r.status_code
    print(status)
    data = r.json()
    return status, data

def send_health_status(health_status):
    print("Sending data to the server")
    data = {
        "feeling" : health_status,
    }
    r = requests.post(URL_POST, json = data)
    status = r.status_code
    print(status)
    return status