import yt_dlp

# Diccionario de videos
videos = {
    "Stressed Out": "https://www.youtube.com/watch?v=pXRviuL6vMY",
    "Overcompensate": "https://www.youtube.com/watch?v=53tgVlXBZVg",
    "Another One Bites The Dust": "https://www.youtube.com/watch?v=JDaD2G9xjMc",
    "Devil In You Heart": "https://www.youtube.com/watch?v=YQ-KG2Eda-c"
}


# Función para seleccionar un video
def _select_video():
    option = 0
    while option < 1 or option > len(videos):
        for i, title in enumerate(videos, start=1):
            print(f"{i}. {title}")
        option = input("Seleccione un video indicando el número de delante: ")
        if option.isdigit():
            option = int(option)
            if option < 1 or option > len(videos):
                print(f"Por favor ingrese un número válido (1-{len(videos)})")
        else:
            option = 0
            print("Por favor indique números enteros")
    return option


# Seleccionar video
option_video = _select_video()
key = list(videos.keys())[option_video - 1]
url = videos[key]

# Selección de formato
video_format = input(
    "Seleccione cómo descargar el video\n1. Video y audio\n2. Solo audio (mp3)\nOpción: ")

# Configurar opciones según la elección
if video_format == "2":
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'../../assets/example/videos/{key}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
else:
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'../../assets/example/videos/{key}.%(ext)s'
    }

# Descargar usando yt-dlp
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
