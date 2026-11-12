import requests
response=requests.head("https://httpbin.org/get")
print(response.status_code)
print(response.url)
print(response.text)
print(response.headers)