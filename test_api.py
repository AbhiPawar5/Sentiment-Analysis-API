import requests
import json

heroku_url = 'https://vast-river-42197.herokuapp.com/api'
data = {"query":"That movie was boring!"}

response = requests.get(heroku_url, data)

print("Status Code : ", response)
print("\nResponse : ",response.text)

print("\nSentiment Result : ",response.json()['sentiment_result'])
print("\nProfanity Result : ",response.json()['profanity_result'])