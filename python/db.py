from pymongo import MongoClient, errors
from bson.json_util import dumps
import os


MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.m3fek.mongodb.net/sample_restaurants"
client = MongoClient(uri, username='ds2022', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
sampler = client.sample_restaurants
restaurants = sampler.restaurants