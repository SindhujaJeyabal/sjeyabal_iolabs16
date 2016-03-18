import pymongo
from bson.son import SON

#gets you the handler on the mongo client
client = pymongo.MongoClient()
#choose the data base
db = client.Surveys
#choose the collection
collection = db.userdetails

#example code
def InsertDummyRecords():
	collection.insert({"driverID" : "JohnD@example.com", "start_long" : "33.2991"})
# if __name__ == "__main__":
# 	InsertDummyRecords()

def insert_result(uname, email, surveyResponse):
	print uname, email, surveyResponse
	collection.insert({\
			'user_name': uname,\
			'user_email': email,\
			'color': surveyResponse['color'],\
			'food': surveyResponse['food'],\
			'vacation': surveyResponse['vacation'],\
			'fe-before': float(surveyResponse['fe-before']),\
			'fe-after': float(surveyResponse['fe-after']),\
			'interest': surveyResponse['interest'].strip(),\
			'comment': surveyResponse['comment'].strip()
			 })

def get_aggregate():
	aggregate = {}
	pipeline = [{"$group": {"_id": "null","avg_before": {"$avg": "$fe-before"}, "avg_after": {"$avg": "$fe-after"}}}]
	aggregate["count"] = collection.count()
	pipeline_result  = list(collection.aggregate(pipeline))[0]
	aggregate["avg_before"] = pipeline_result["avg_before"]
	aggregate["avg_after"] = pipeline_result["avg_after"]
	print aggregate
	return aggregate
