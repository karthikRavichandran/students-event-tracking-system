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

# Example usage:
collection_name = 'students' 
csv_file_path = 'data.csv'  
service_account_key = 'serviceAccount.json'  

#  Ecapsulating this functionality, making it reusable and modular
export_firestore_collection_to_csv(collection_name, csv_file_path, service_account_key)
