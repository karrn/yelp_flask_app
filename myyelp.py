from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def results(location, term):
	#Yelp API credentials
	auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    token=os.environ['TOKEN'],
    token_secret=os.environ['TOKEN_SECRET']
	)

	#Google API key
	google_key = os.environ['GOOGLE_API_KEY']

	client = Client(auth)

	#Yelp API search parameters
	params = {
	    'lang': 'en',
	    'limit': 7
	}

	businesses = []

	params['term'] = term
	response = client.search(location, **params)
	for business in response.businesses:
		businesses.append({"name": business.name, 
            "rating": business.rating, 
            "phone": business.phone,
            "tip":business.snippet_text,
            "reviews":business.review_count,
            "address":business.location.display_address,
            "image":business.image_url,
            "map_url": "https://www.google.com/maps/embed/v1/place?key=" + str(google_key) + "&q=" + str(business.location.display_address)
        })
	return businesses