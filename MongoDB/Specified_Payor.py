from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["Bank_Statements"]  

collection = db["Money_In"]  

payor = "Sze Ho Pok" #change here

# Define Aggregation Pipeline
pipeline = [
    {
        "$match": {
            "Description": {"$regex": payor} #specified payee
        }
    },
    {
        "$group": {
            "_id": "$Description",
            "Total": {"$sum": "$Money In"},
            "All_Transaction": {"$push": "$Money In"},
            "Dates" : {"$push" : "$Date"}
        }
    },
    {
        "$project": {
            "_id": 1,
            "Total": {"$round": ["$Total", 2]},
            "All_Transaction": 1,
            "Dates":1
        }
    }
]

# Execute Aggregation
result = list(collection.aggregate(pipeline))

print(payor)
for i in result:
    print(i)
