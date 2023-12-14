# Python code for implementing the modularity feature and to download the structured data from Firestore DB in a .csv format.
import sys
sys.path.append('../../')
import requests
import csv
import json
from firebase_admin import credentials, firestore, initialize_app

class DownloadDataFirebase:
    """
    The DownloadDataFirebase object loads in the data from the Firebase 
    cloud storage and stores it locally on the user's computer.

    ...

    Attributes
    ----------
    cred : firebase_admin.credentials.Certificate
        The credentials required to access the firebase cloud
    firebase_app : firebase_admin.App
        The firebase application which accesses the database
    db: google.cloud.firestore.Firestore
        The loaded database from the cloud
    Methods
    -------
    __out_dirs()
        Set the output directories to write to
    __in_firebase_url()
        Set the endpoints for our firebase access
    import_firestore_collection_to_csv(collection_name, csv_file_path)
        Take the firebase cloud data and store it locally as a csv
    import_firebase_collection_to_json(data_endpoint, file, download_path)
        Take the firebase cloud data and store it locally as a json
    download_all_json()
        Iterate through the relevant json files and download them all locally
    download_csv()
        Iterate through the relevant csv files and download them all locally
    """

    def __init__(self):
        """
        Initialize the firebase objects and credentials as well as the relevant endpoints/directories.
        """
        self.cred = credentials.Certificate('../../data/serviceAccount.json')  # Replace with your service account key
        self.firebase_app = initialize_app(self.cred)
        self.db = firestore.client()
        self.__in_firebase_url()
        self.__out_dirs()



    def __out_dirs(self):
        """
        Set the output directories to write to
        """
        self.data_root_folder = '../../data'
        self.gradescope_dir = self.data_root_folder + '/gradescope/'
        self.dashboard_dir = self.data_root_folder + '/dashboard/'
        self.moodle_dir = self.data_root_folder + '/moodle/'
        self.piazza_dir = self.data_root_folder + '/piazza/'
        self.logins = self.data_root_folder + '/logins.csv'
        self.students = self.data_root_folder + '/students.csv'


    def __in_firebase_url(self):
        """
        Set the endpoints for our firebase access
        """
        self.firebase_url = 'https://pip-install-project520-default-rtdb.firebaseio.com/'
        self.project_endpoint= 'Student Event Tracking System Database /'
        self.gradescope_endpoint = self.firebase_url + self.project_endpoint + 'Gradescope/'
        self.moodle_endpoint = self.firebase_url + self.project_endpoint + 'Moodle/'
        self.piazza_endpoint = self.firebase_url + self.project_endpoint + 'Piazza/'
        self.dashboard_endpoint = self.firebase_url + self.project_endpoint + 'Dashboard/'

    def import_firestore_collection_to_csv(self, collection_name, csv_file_path):
        """
        Take the firebase cloud data and store it locally as a csv
        
        Parameters
        ----------
        collection_name : str
            The collection name from which we are reading in the cloud
        csv_file_path : str
            The file path which we are writing the collection to locally
        """
        # Get all documents from the specified collection
        collection_ref = self.db.collection(collection_name)
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

    def import_firebase_collection_to_json(self, data_endpoint, file, download_path = 'gradescope_math.json'):
        """
        Take the firebase cloud data and store it locally as a json
        
        Parameters
        ----------
        data_endpoint : str
            The data endpoint we will access
        file : str
            The name of the file we are reading
        download_path : str
            The path to which we are downloading the object
        
        Returns
        -------
        int
            0 for successful fetch, 1 otherwise
        """
        response = requests.get(data_endpoint + file + '.json')
        # response = requests.get(self.firebase_url + 'Student Event Tracking System Database /Gradescope/math314.json')

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()
            if isinstance(data, list):
                data = data[0]
            elif not isinstance(data, dict):
                return 0
            json_data = json.dumps(data)  # 'indent' for pretty formatting (optional)

            # Writing JSON data to a file
            with open(download_path + file + '.json', 'w') as json_file:
                json_file.write(json_data)
            # Now 'data' contains the JSON data from the specified endpoint
            # print("Data from Firebase Realtime Database:")
            print(f"Data Downloaded in the path : {download_path}")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return 1
        return 0

    def download_all_json(self):
        """
        Iterate through the relevant json files and download them all locally
        """
        courses = ['math314', 'phys999', 'lang101']
        for course in courses:
            self.import_firebase_collection_to_json(self.gradescope_endpoint, course, self.gradescope_dir)
            self.import_firebase_collection_to_json(self.piazza_endpoint, course, self.piazza_dir)
            self.import_firebase_collection_to_json(self.moodle_endpoint, course, self.moodle_dir)

        self.import_firebase_collection_to_json(self.dashboard_endpoint, 'dashboard', self.dashboard_dir)

    def download_csv(self):
        """
        Iterate through the relevant csv files and download them all locally
        """
        self.import_firestore_collection_to_csv('logins', self.logins)
        self.import_firestore_collection_to_csv('students', self.students)


if __name__ == '__main__':
    download_data = DownloadDataFirebase()
    download_data.download_all_json()
    download_data.download_csv()