from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["Bank_Statements"]  
collection = db["Money_Out"]  

# Define Aggregation Pipeline
pipeline = [
    {
        "$group": {
            "_id": None,
            "Total": {"$sum": "$Money Out"},
        }
    },
    {
        "$project": {"_id": 0}
    }
]

# Execute Aggregation
result = list(collection.aggregate(pipeline))

print("Total Expense:")
for i in result:
    print(i)
