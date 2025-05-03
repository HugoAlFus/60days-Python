import requests

URL = "https://icanhazdadjoke.com/"

HEADERS = {
    "Accept": "application/json"
}

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    joke = response.json()
    print(f"Chiste: {joke["joke"]}")
else:
    print("No se puedo obtener un chiste")