from langdetect import detect
from textblob import TextBlob
from googletrans import Translator

txt = input("Introduce el texto el cual queres que sea analizado. Se obtendrá el idio y los sentimientos que haya en "
            "el texto:\n")
print(f"\nEl idioma usado es {detect(txt)}")

translator = Translator()
translated = translator.translate(txt, dest='en').text

blob = TextBlob(translated)

pol = blob.sentiment.polarity
subj = blob.sentiment.subjectivity

if pol > 0.1:
    tipo = "Positivo"
elif pol < -0.1:
    tipo = "Negativo"
else:
    tipo = "Neutral"

print(f"🔍 Análisis de sentimientos:")
print(f"   → Polaridad: {pol:.2f} ({tipo})")
print(f"   → Subjetividad: {subj:.2f}")
