import time
import requests
import os
import json

def auth():
  return os.environ.get("BEARER_TOKEN")

def url(next_token):
  query = "Jade Picon"
  tweet_fields = "tweet.fields=author_id"
  url_formatada = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}"
  if next_token:
    url_formatada += f"&next_token={next_token}"
  return url_formatada

def headers(bearer_token):
  return {"Authorization": f"Bearer {bearer_token}"}

def lerDados(next_token=None):
  response = requests.request("GET", url(next_token), headers=headers(auth()))
  print(response.status_code)

  body = response.json()

  for dado in body["data"]:
    print(f"Author ID: {dado['author_id']}")
    print(f"Tweet: {dado['text']}")
    print("---------------------------")

  if body["meta"]["next_token"]:
    print(f"============= lendo proxima página ============= ")
    time.sleep(2)
    lerDados(body["meta"]["next_token"])

lerDados()