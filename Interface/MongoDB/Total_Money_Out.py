from pymongo import MongoClient

def Out_monthly(date):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27018/")
    db = client["Personal_Accounting"]  
    collection = db["Full_Detail"]  

    # Define Aggregation Pipeline
    pipeline = [
            {
            "$match": {
                "Date": { "$regex": date } 
            }
        },
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

    if not result:
            return 0  # If no documents matched, return 0

    return result[0]["Total"]  # Just return the total number
        
