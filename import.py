import request
url = "https://jsonplaceholder.typicode.com/users"
reponse=request.get(url)
print(reponse.status_code)
print(reponse.json())
lll