import requests
import socket

res = socket.gethostbyname(socket.gethostname())
print(res)

# send request post to res
user_info = {'file': '3'}
r = requests.post("http://{}:7399/register".format(res), data=user_info)
# get return info from server.py
print(r.text)
