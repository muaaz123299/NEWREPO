import requests
student={
    "course":"ai automation"
}
response=requests.patch("https://httpbin.org/patch",json=student)
response.raise_for_status()
print(response.status_code)
print(response.url)
print(response.text)
print(response.json())
print(response.headers)