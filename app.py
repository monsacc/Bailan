import requests
import json

r = requests.get("http://127.0.0.1:8000/todo")
print(r)
print(r.json())