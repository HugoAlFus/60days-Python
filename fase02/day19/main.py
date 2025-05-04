import requests
import urllib.parse

track = input("Introduzca el nombre de la canción: ")
artist = input("Introduzca el artista: ")


query = f'track:"{track}" AND artist:"{artist}"'
encoded_query = urllib.parse.quote(query)

url = f"https://musicbrainz.org/ws/2/recording/?query={encoded_query}&fmt=json"

headers = {
    "User-Agent": "MyPythonApp/1.0 (hugoalfus@gmail.com)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    recordings = data.get("recordings", [])

    if recordings:
        for rec in recordings[:1]:
            title = rec.get("title", "Desconocido")
            artists = ", ".join(artist["name"] for artist in rec.get("artist-credit", []))
            print(f"Título: {title}")
            print(f"Artista(s): {artists}")
            print(f"ID: {rec.get('id')}")
            print("-" * 40)
    else:
        print("No se encontraron resultados.")
else:
    print(f"Error {response.status_code}: No se pudo conectar con MusicBrainz.")
