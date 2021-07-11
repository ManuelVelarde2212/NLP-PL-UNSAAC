import tweepy
import json
# claves personales
from Keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

#Obtener mi informacion
""" data = api.me()
print(data) """

# Obtener informacion de otro usuario
""" data = api.get_user("nvidia")
print(json.dumps(data._json, indent=2)) """

# Obtener seguidores de un usuario
""" data = api.followers(screen_name = "nvidia")
print(data)
for usuario in data:
    print(json.dumps(usuario._json, indent=2)) """

# Obtener friends/followees de un usuario utilizando Cursor
""" for usuario in tweepy.Cursor(api.friends, screen_name='nvidia').items(2):
    print(json.dumps(usuario._json, indent=2)) """

# Obtener un timeline
""" for tweet in tweepy.Cursor(api.user_timeline,screen_name='nvidia', tweet_mode='extended').items(5):
    print(json.dumps(tweet.full_text, indent=2)+'\n') """

# Buscar Tweets
""" for tweet in tweepy.Cursor(api.search, q='elecciones peru', tweet_mode = 'extended').items(1):
    print(json.dumps(tweet._json, indent=2)) """
for tweet in tweepy.Cursor(api.search, q='elecciones peru', tweet_mode = 'extended').items(5):
    print(json.dumps(tweet.full_text, indent=2))
