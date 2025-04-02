#!/usr/bin/env python3
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# mongohost should look something like 'mongodb+srv://cluster0.xxxxx.mongodb.net/'
MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)


# mongohost should look something like 'mongodb+srv://cluster0.xxxxx.mongodb.net/'


sampler = client.sample_activities
activities = sampler.activities


new_record = {
    "name": {"dancing"},
      "equipment": {"dance shoes", "leotard"}
}

activities.insert_one(new_record)

#activities.insert_one({"name":"dancing","equipment":["dance shoes", "leotard"]})
#activities.insert_one({"name":"biking","equipment":["bike","helmet","shoes"]})
#activities.insert_one({"name":"gardening","equipment":["shovel","seeds","mulch"]})
#activities.insert_one({"name":"running","equipment":["sneakers", "clothes"]})
#activities.insert_one({"name":"baking","equipment":["oven","ingredients","kitchen tools"]})

query=activities.find().limit(3)

for i in query:
	print(i)

