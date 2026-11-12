import requests
response=requests.options("https://httpbin.org/anything")
print(response.status_code)
print(response.url)
print(response.text)
print(response.headers)