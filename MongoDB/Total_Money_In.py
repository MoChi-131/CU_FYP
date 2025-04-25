from pymongo import MongoClient

def monthly(collection, date):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27018/")
    db = client["Bank_Statements"]  
    collection = db[collection]  

    # Define Aggregation Pipeline
    pipeline = [
            {
            "$match": {
                "Date": { "$regex": date }  # Match dates starting with "2025-01-"
            }
        },
        {
            "$group": {
                "_id": None,
                "Total": {"$sum": "$Money In"},
            }
        },
        {
            "$project": {"_id": 0}
        }
    ]

    # Execute Aggregation
    result = list(collection.aggregate(pipeline))

    print("Total Income:", result)

    return result
        
