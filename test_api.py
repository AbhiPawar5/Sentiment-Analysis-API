import requests
import json

heroku_url = 'https://vast-river-42197.herokuapp.com/' # change to your app name# sample data
data = {"query":"That movie was boring!"}

data = json.dumps(data)

send_request = requests.post(heroku_url, data)
print(send_request)
print("\n\n\n",send_request.text)