from pymongo import MongoClient

def agg_money_in():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27018/")
    db = client["Bank_Statements"]  # Your database
    collection = db["Raw_Data"]  # Replace with your collection

    # Define Aggregation Pipeline
    pipeline = [
        {"$match": {"Money Out": 0}},  # Filter transactions with Money In = 0
        {"$sort": {"Date": 1}},  # Sort by Date in ascending order
        {"$out": "Money_In"}  # Output to a new collection
    ]

    # Execute Aggregation
    collection.aggregate(pipeline)

    print("Aggregation completed. Data saved in 'Money_In' collection.")

    return