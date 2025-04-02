#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# mongohost should look something like 'mongodb+srv://cluster0.xxxxx.mongodb.net/'
MUSER = os.getenv('MUSER')
MPASS = os.getenv('MPASS')
MHOST = os.getenv('MHOST')
client = MongoClient(MHOST, username=MUSER, password=MPASS, connectTimeoutMS=200, retryWrites=True)
sampler = client.sample_activities
activities = sampler.activities


new_record = {
    "name": "running",
      "equipment": ["sneakers", "shorts"]
}
activities.insert_one(new_record)


new_record1 = {
    "name": "painting",
      "equipment": ["paintbrush", "paint"]
}
activities.insert_one(new_record1)


new_record2 = {
    "name": "biking",
      "equipment": ["bike", "helmet"]
}
activities.insert_one(new_record2)


new_record3 = {
    "name": "dancing",
      "equipment": ["shoes", "leotard"]
}
activities.insert_one(new_record3)


new_record4 = {
    "name": "baking",
      "equipment": ["ingredients", "oven"]
}
activities.insert_one(new_record4)



activities.delete_many({"name": "swimming"}) #needed to do this because swimming kept popping up (https://www.mongodb.com/docs/manual/tutorial/remove-documents/?msockid=28e5b96d2c1a6e6d0c2ca8d62dcc6f88)


queries=activities.find().limit(3)


for i in queries:
	print(i)



