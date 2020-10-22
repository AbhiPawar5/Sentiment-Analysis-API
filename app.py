import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from profanity import profanity 

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictSentiment(Resource):
	"""GET Method to return the sentiment and profanity of the query sentence"""
	def get(self):
		output = {}
		prof_dict = {}
		
		args = parser.parse_args()
		user_query = args['query']

		sid = SentimentIntensityAnalyzer()
		pred = sid.polarity_scores(user_query)

		if profanity.contains_profanity(user_query):
			prof_dict['profanity_check'] = True
			prof_dict['profanity_censored'] = profanity.censor(user_query) 

			output['profanity_result'] = prof_dict

		else:
			prof_dict['profanity_check'] = False
			output['profanity_result'] = prof_dict

		output['sentiment_result'] = pred
		return jsonify(output)


api.add_resource(PredictSentiment, '/')

if __name__ == '__main__':
	app.run(debug=True)