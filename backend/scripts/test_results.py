import requests

def test():
    url = "http://127.0.0.1:8000/api/v1/generate-sql"
    data = {"prompt": "Dime los 5 jugadores con más goles"}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    test()
