from pymongo import MongoClient

def Full_Out():

    client = MongoClient("mongodb://localhost:27018/")
    db = client["Personal_Accounting"]  # Your database
    collection = db["Money_Out"]  # Replace with your collection

    pipeline = [
        {
            "$lookup": {
                "from": "Reciept_Full_Detail",
                "let": {
                    "desc": "$Description",
                    "money_out": "$Money Out"
                },
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {
                                "$and": [
                                    {
                                        "$regexMatch": {
                                            "input": "$Supplier Name",
                                            "regex": { "$concat": [".*", { "$trim": { "input": "$$desc" } }, ".*"] },
                                            "options": "i"
                                        }
                                    },
                                    {
                                        "$eq": ["$Total Amount", "$$money_out"]
                                    }
                                ]
                            }
                        }
                    }
                ],
                "as": "Reciept"
            }
        },
        {
            "$addFields": {
                "Category": {
                    "$cond": {
                        "if": {"$gt": [{"$size": "$Reciept"}, 0]},
                        "then": {"$arrayElemAt": ["$Reciept.Category", 0]},
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