import requests

response=requests.get("https://www.google.com")
print(response.status_code)
print(response)
print(response.content)