import requests

# API endpoint
url = "https://p7evogw7di.execute-api.us-east-1.amazonaws.com/test/movies"

# GET request to the API
response = requests.get(url)
# printing the status code
print(response.status_code)

# printing the content
print(response.content)

# response outputs a bytes
res_str = response.content.decode()
print(res_str)
print(type(res_str))

# returns json encoded content
res_json = response.json()
# list
print(type(res_json))
print(res_json)
print("*"*65)

# Get movies
# looping the res_json
for movie in res_json:
    print(movie)
    print(movie.get("MovieName"))
    # dict
    print(type(movie))
    print("==="* 40)