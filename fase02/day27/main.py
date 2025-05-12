from gtts import gTTS
audio = "../../assets/example/videos/convertido_de_texto.mp3"

text = input("Introduzca el texto que quiere convertir a audio: ")

tts = gTTS(text=text, lang='es')
tts.save(audio)

print("Aundio guardado en assets, example, video como 'convertido_de_texto.mp3'")