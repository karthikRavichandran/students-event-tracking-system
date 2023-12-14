# Python code for implementing the modularity feature and to download the structured data from Firestore DB in a .csv format.
 
import csv
from firebase_admin import credentials, firestore, initialize_app

# Function to export Firestore collection to CSV
def export_firestore_collection_to_csv(collection_name, csv_file_path, service_account_key):
 
    cred = credentials.Certificate(service_account_key)
    firebase_app = initialize_app(cred)
    db = firestore.client()

    # Get all documents from the specified collection
    collection_ref = db.collection(collection_name)
    documents = collection_ref.stream()

    # Write Firestore data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[], extrasaction='ignore')

        # Iterate through documents to get field names and write data to CSV
        for doc in documents:
            data = doc.to_dict()
            if len(writer.fieldnames) == 0:
                writer.fieldnames = list(data.keys())
                writer.writeheader()
            writer.writerow(data)

    print(f"CSV file '{csv_file_path}' has been created with Firestore data.")


# For downloading the json from firestore DB

import json
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore with credentials
#cred = credentials.Certificate('serviceAccount.json')  # Replace with your service account key
#firebase_app = initialize_app(cred)
db = firestore.client()

# Replace 'your_collection_name' with the name of your Firestore collection
collection_name = 'test'

# Get all documents from the specified collection
collection_ref = db.collection(collection_name)
documents = collection_ref.stream()

# Define the path where you want to save the JSON file
json_file_path = 'gradescope_math.json'  # Replace with your desired path and file name

# Extract Firestore data and write it to a JSON file
data_to_export = {}
for doc in documents:
    doc_data = doc.to_dict()
    data_to_export[doc.id] = doc_data

with open(json_file_path, 'w') as json_file:
    json.dump(data_to_export, json_file, indent=4)

print(f"JSON file '{json_file_path}' has been created with Firestore data.")
