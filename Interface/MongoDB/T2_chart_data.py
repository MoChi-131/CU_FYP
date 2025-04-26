from pymongo import MongoClient
from datetime import datetime
from dateutil.relativedelta import relativedelta

def retrieve_expense_data(current_date=None):
    # Use provided date or default to test date
    if current_date is None:
        current_date = datetime(2025, 4, 20)  # Replace with datetime.now() for real-time use
    
    # Define categories
    categories = ["toll", "food", "parking", "transport", "accommodation", "gasoline", "telecom", "miscellaneous"]
    
    # Calculate date range for last month
    last_month_end = current_date.replace(day=1) - relativedelta(days=1)  # Last day of last month
    last_month_start = last_month_end.replace(day=1)  # First day of last month
    
    # Initialize category totals
    category_totals = {category: 0.0 for category in categories}
    
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27018/")
        db = client["Personal_Accounting"]
        collection = db["Reciept_Full_Detail"]
        
        # Aggregation pipeline for last month
        pipeline = [
            {
                "$match": {
                    "Date": {
                        "$gte": last_month_start.strftime('%Y-%m-%d'),
                        "$lte": last_month_end.strftime('%Y-%m-%d')
                    }
                }
            },
            {
                "$group": {
                    "_id": "$Category",
                    "total_amount": {"$sum": "$Total Amount"}
                }
            }
        ]
        
        # Execute pipeline
        results = collection.aggregate(pipeline)
        
        # Process results
        for result in results:
            category = result['_id']
            if category in categories:  # Only include specified categories
                category_totals[category] = round(result['total_amount'], 2)
        
        # Close MongoDB connection
        client.close()
        
    except Exception as e:
        print(f"Error connecting to MongoDB or processing data: {e}")
        return None
    
    # Return data
    # Convert category totals to ordered list
    data = [category_totals[category] for category in categories]
    print(data)
    return data
    
if __name__== "__main__":
    print(retrieve_expense_data())