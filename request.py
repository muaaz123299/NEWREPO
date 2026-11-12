import requests
student={
    "name":"muaaz",
    "age": 18,
    "class":"bs english"
}
r=requests.post("https://httpbin.org/post",json=student)
print(r.status_code)
a=requests.get("https://httpbin.org/get")
print(r.status_code)
student={
    "sem":3
}
c=requests.put("https://httpbin.org/post",json=student)
print(r.status_code)
print(r.headers)