import requests

def get_header():
    url = "http://ihrm-test.itheima.net/api/sys/login"
    data = {"mobile": "13800000002", "password": "123456"}
    resp = requests.post(url=url, json=data)
    print(resp.json())
    token=resp.json().get("data")
    header={"Content-Type":"application/json", "Authorization":"Bearer"+" "+token}
    return header