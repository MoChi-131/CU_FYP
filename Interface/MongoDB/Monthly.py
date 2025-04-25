from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["Bank_Statements"]  

collection = "Money_Out"
collection = db[collection]  

# Define Aggregation Pipeline
pipeline_month = [
    {
        "$match": {
            "Date": { "$regex": "2025-01-" }  # Match dates starting with "2025-01-"
        }
    },
    {
        "$project": {"_id": 0}  # exclude _id from results
    }
]

# Execute Aggregation
result_month = list(collection.aggregate(pipeline_month))

print("Grouped by Year-Month:")
for i in result_month:
    print(i)
