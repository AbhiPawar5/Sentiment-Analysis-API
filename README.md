# Sentiment and Profanity Analysis API using Flask and Python
This API is developed to explore more about Flask and RESTful APIs.

## Getting started with Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

Flask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004.According to Ronacher, the idea was originally an April Fool's joke that was popular enough to make into a serious application.

## API URL
Try this API on : https://vast-river-42197.herokuapp.com/api
 
### Running on your station
Recommend using [Anaconda](https://www.anaconda.com/distribution/). Anaconda does not come with Flask/Requests, so you will need to install those seperately. 
```
pip install flask flask_restful nltk profanity
```
For additional information on installing Flask & Profanity: [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Profanity](https://pypi.org/project/profanity/)
```
python test_api.py
```

### Example request
Using CURL:
```
curl -X GET https://vast-river-42197.herokuapp.com/api -d query='I love that movie!'
curl -X GET https://vast-river-42197.herokuapp.com/api -d query='that movie was shit!'
```

Using Python:
```
heroku_url = 'https://vast-river-42197.herokuapp.com/api'
data = {"query":"I love that movie!"}
response = requests.get(heroku_url, data)
```

### Example response 
```
{
"profanity_result": {"profanity_check":false},
"sentiment_result": {"compound":0.6696,"neg":0.0,"neu":0.308,"pos":0.692}
}

{
"profanity_result": {"profanity_censored":"that movie was @%@!","profanity_check":true},
"sentiment_result": {"compound":0.0,"neg":0.0,"neu":1.0,"pos":0.0}
}
```
