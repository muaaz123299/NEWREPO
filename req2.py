import requests
student={
    "age":19,
    "course":"python automation",
    "semester":4
}
response=requests.put("https://httpbin.org/put",json=student)
print(response.status_code)
print(response.url)
print(response.text)
print(response.json())
print(response.headers)