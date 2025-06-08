import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

# Autenticación con OAuth 1.0a
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    bearer_token=os.getenv("BEARER_TOKEN")
)

username = "Hugoelcrack12"

try:
    # Primero obtenemos el id de usuario por username
    user = client.get_user(username=username)
    user_id = user.data.id
    print(f"User ID: {user_id}")

    # Ahora obtenemos los últimos tweets del usuario
    tweets = client.get_users_tweets(user_id, max_results=5)  # Cambia el número si quieres más

    print("Últimos tweets:")
    for tweet in tweets.data:
        print(f"ID: {tweet.id} - Texto: {tweet.text}")

except Exception as e:
    print(f"Ocurrió un error: {e}")
