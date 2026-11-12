import requests
response=requests.delete("https://httpbin.org/delete")
response.raise_for_status()
print(response.status_code)
print(response.url)
print(response.text)
print(response.json())
print(response.headers)
