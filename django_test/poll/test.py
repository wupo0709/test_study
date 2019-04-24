import requests
import json


user = {"username":"admin", "password":"123456"}


ret_get = requests.get("http://172.18.58.217:8052")
if ret_get.status_code == 200:
    ret_post = requests.post('http://172.18.58.217:8052/login', data=user)
    print(ret_post.text)
else:
    print("false to connection")
