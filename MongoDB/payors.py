from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["Bank_Statements"]  
collection = db["Money_In"]  

# Define Aggregation Pipeline
pipeline = [
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
    },
    {
        "$sort": {
            "Total" : -1
        }
    }
]

# Execute Aggregation
result = list(collection.aggregate(pipeline))

print("Grouped by Payors:")
for i in result:
    print(i)
    print()
