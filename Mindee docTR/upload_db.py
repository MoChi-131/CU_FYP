import pandas as pd
import pymongo

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27018/")  # Change to your MongoDB URI
db = client["Receipts"]  # Database Name

# Function to load CSV into MongoDB
def load_csv_to_mongo(csv_file, collection_name):
    # Load CSV into DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to Dictionary for MongoDB
    records = df.to_dict(orient="records")

    # Get collection and insert data
    collection = db[collection_name]
    collection.insert_many(records)

    print(f"Data from {csv_file} successfully inserted into {collection_name}!")

# Insert data into Raw_Data_Details collection
load_csv_to_mongo(r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Mindee docTR\Receipt_Detail.csv", 'Raw_Data_Details')

# Insert data into Raw_Data_Items collection
load_csv_to_mongo(r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Mindee docTR\Receipt_Items.csv", 'Raw_Data_Items')
