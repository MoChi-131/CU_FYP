from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["Bank_Statements"]  

collection = db["Money_Out"]  

payee = "TS Kwong" #change here

# Define Aggregation Pipeline
pipeline = [
    {
        "$match": {
            "Description": {"$regex": payee} #specified payee
        }
    },
    {
        "$group": {
            "_id": "$Description",
            "Total": {"$sum": "$Money Out"},
            "All_Transaction": {"$push": "$Money Out"},
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

print(payee)
for i in result:
    print(i)
