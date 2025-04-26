from pymongo import MongoClient

def agg_money_out():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27018/")
    db = client["Bank_Statements"]  # Your database
    collection = db["Raw_Data"]  # Replace with your collection

    # Define Aggregation Pipeline
    pipeline = [
        {"$match": {"Money In": 0}},  # Filter transactions with Money In = 0
        {"$sort": {"Date": 1}},  # Sort by Date in ascending order
        {"$out": "Money_Out"}  # Output to a new collection
    ]

    # Execute Aggregation
    collection.aggregate(pipeline)

    print("Aggregation completed. Data saved in 'Money_Out' collection.")
    
    return
