import requests
student={
    "name":"muaaz",
    "age":18,
    "course":"python",
    "semester":3
}
response=requests.post("https://httpbin.org/post",json=student)
response.raise_for_status
print(response.status_code)
print(response.url)
print(response.text)
print(response.json())
print(response.headers)
