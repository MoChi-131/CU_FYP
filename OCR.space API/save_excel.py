import pandas as pd
import pymongo
import pandas as pd

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27018/")  # Change to your MongoDB URI
db = client["Bank_Statements"]  # Database Name
collection = db["Raw_Data"]  # Collection Name


# File names
excel_file = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\OCR.space API\extracted_data.xlsx"  # Updated Excel file
csv_file = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\OCR.space API\output_csv\Finalised.csv"  # Output CSV file

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
