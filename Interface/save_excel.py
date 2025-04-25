import pandas as pd
import pymongo
import pandas as pd
import os

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27018/")  # Change to your MongoDB URI
db = client["Bank_Statements"]  # Database Name
collection = db["Raw_Data"]  # Collection Name

def upload_excel():
    # File names
    current_dir = os.path.dirname(os.path.abspath(__file__))
    excel_file = os.getenv("EXCEL_FILE") or os.path.join(current_dir, 'extracted_data.xlsx')
    csv_file = os.getenv("CSV_FILE") or os.path.join(current_dir, 'OCR', 'output_csv', 'Finalised.csv')
    
    # Read the updated Excel file
    df = pd.read_excel(excel_file, engine='openpyxl')

    # Save the updated data back to CSV
    df.to_csv(csv_file, index=False)

    print(f"CSV file successfully updated from Excel: {csv_file}")

    # Load CSV into a DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to Dictionary for MongoDB
    records = df.to_dict(orient="records")

    # Insert into MongoDB
    collection.insert_many(records)

    print("CSV data successfully inserted into MongoDB!")
