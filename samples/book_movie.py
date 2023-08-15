import requests


def get_response():
    # API Endpoint
    url = "https://d6gop81pck.execute-api.ap-south-1.amazonaws.com/test/movies"

    response = requests.get(url)
    res_json = response.json()
    return res_json




if __name__ == "__main__":
    print("------------------- Welcome to Book My Movie -------------------------")
    print("Movies in Theatre")
    print("1. Bro \n 2. Baby \n 3.Samajavaragamana \n")
    movie_id = int(input("Select movie \n"))
    if movie_id == 1:
        movie_name = "Bro"
    elif movie_id == 2:
        movie_name = "Baby"
    elif movie_id == 3:
        movie_name = "Samajavaragamana"
    else:
        movie_name = -1
