import requests

response = requests.get("https://www.jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
