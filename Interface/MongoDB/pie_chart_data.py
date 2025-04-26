from pymongo import MongoClient

categories = ["toll", "food", "parking", "transport", "accommodation", "gasoline", "telecom", "miscellaneous"]

def fetch_category_data(date):
    data = []

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27018/")
    db = client["Personal_Accounting"]
    collection = db["Reciept_Full_Detail"]

    for category in categories:
        pipeline = [
            {
                "$match": {
                    "Category": category,
                    "Date": {
                        "$regex": date
                    }
                }
            },
            {
                "$group": {
                    "_id": "$Category",
                    "total_amount": {
                        "$sum": "$Total Amount"
                    }
                }
            }
        ]

        result = list(collection.aggregate(pipeline))
        amount = result[0]["total_amount"] if result else 0
        data.append(amount)

    return data, categories
