from pymongo import MongoClient

def Full_Out():

    client = MongoClient("mongodb://localhost:27018/")
    db = client["Personal_Accounting"]  # Your database
    collection = db["Money_Out"]  # Replace with your collection

    pipeline = [
        {
            "$lookup": {
                "from": "Reciept_Full_Detail",
                "localField": "Description",
                "foreignField": "Supplier Name",
                "as": "Reciept"
            }
        },
        {
            "$addFields": {
                "Category": {
                    "$cond": {
                        "if": {
                            "$gt": [
                                {
                                    "$size": "$Reciept"
                                },
                                0
                            ]
                        },
                        "then": {
                            "$arrayElemAt": ["$Reciept.Category", 0]
                        },
                        "else": "other"
                    }
                }
            }
        },
        {
            "$out": {
                "db": "Personal_Accounting",
                "coll": "Full_Detail"
            }
        }
    ]

    print("Saved in Full_Detail")
    
    return collection.aggregate(pipeline)