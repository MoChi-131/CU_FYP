# Pui Chi Angie_FYP

!!Commands to set up environment:
python3 -m venv venv
venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt


1: Install MongoDB from offical website

2: Create a new connection and a database named "Personal_Accounting"

3: Start your database
For example: & "C:\Program Files\MongoDB\Server\8.0\bin\mongod.exe" --port 27017 --dbpath="C:\data\db"

3: Replace your connection host id in all python scipts in the folder of "MongoDB"
For example - 
    client = MongoClient("mongodb://localhost:27018/")
    db = client["Personal_Accounting"]  
    ## Replce client = MongoClient(<your host id>)

4: Create collections for inserting dummy data
-"Receipt"
-"Budget" 

4: Insert dummy data from "MongoDB/Dummy_data" to "Receipt"

5: Insert pre-set budget plans from "MongoDB/Budget_data"

6: Activiate environment
venv\Scripts\activate

7: Start Flask
python .\flask_fyp.py


