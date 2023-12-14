# Python code for implementing the modularity feature and to download the structured data from Firestore DB in a .csv format.
 
import csv
from firebase_admin import credentials, firestore, initialize_app

class FirebaseDataLoader:
    def __init__(self, service_account_key):
        self.service_account_key = service_account_key

    def export_collection_to_csv(self, collection_name, csv_file_path):
        cred = credentials.Certificate(self.service_account_key)
        firebase_app = initialize_app(cred)
        db = firestore.client()

        collection_ref = db.collection(collection_name)
        documents = collection_ref.stream()

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[], extrasaction='ignore')

            for doc in documents:
                data = doc.to_dict()
                if len(writer.fieldnames) == 0:
                    writer.fieldnames = list(data.keys())
                    writer.writeheader()
                writer.writerow(data)

        print(f"CSV file '{csv_file_path}' has been created with Firestore data.")

# Example usage:
service_account_key = 'serviceAccount.json' 
# created firebase instance of class FirebaseDataLoader,invoking its defined methods.
firebase = FirebaseDataLoader(service_account_key)
collection_name = 'students'
csv_file_path = 'data.csv'

#  Ecapsulating this functionality, making it reusable and modular
firebase.export_collection_to_csv(collection_name, csv_file_path)
