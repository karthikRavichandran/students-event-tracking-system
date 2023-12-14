import unittest
import json
import sys
sys.path.append('../')
from src.database.dataloader import Dataloader

import unittest
import os
import requests
import pandas as pd
import unittest
from selenium import webdriver


#unit test cases to assert if the number of columns are same or not
class TestDataloader(unittest.TestCase):

    def setUp(self):
        self.dataloader = Dataloader(student_id=1001)

    def test_get_moodle_data_columns(self):
        json_file_path = '../data/moodle/lang101.json'
        _, moodle_df, _, _ = self.dataloader.get_moodle_data(json_file_path)

        expected_columns = ['Title', 'Description', 'Due Date']
        actual_columns = list(moodle_df.columns)

        self.assertEqual(expected_columns, actual_columns, "Columns in moodle_df are not as expected")

    def test_get_gradescope_data_columns(self):
        json_file_path = '../data/gradescope/math314.json'
        hws, _, _ = self.dataloader.get_gradescope_data(json_file_path)

        expected_columns = ['Title', 'Description', 'Due Date']  # Replace with expected columns
        actual_columns = list(hws.columns)

        self.assertEqual(expected_columns, actual_columns, "Columns in hws are not as expected")

    def test_get_piazza_df_columns(self):
        json_file_path = '../data/piazza/math314.json'
        piazza_df = self.dataloader.get_piazza_df(json_file_path)

        expected_columns = ['title', 'topic', 'poster', 'poster_date', 'body', 'follow_up_1', 'follow_up_2',
                            'follow_up_3', 'follow_up_4']
        actual_columns = list(piazza_df.columns)

        self.assertEqual(expected_columns, actual_columns, "Columns in piazza_df are not as expected")


#unit test case for calling the OpenAI API and checking if the status code is 200,
class TestOpenAIAPI(unittest.TestCase):

    def setUp(self):
        # Set your OpenAI GPT-3.5 API key
        self.api_key = os.environ['OPENAI_API_KEY']
        self.openai_endpoint = 'https://api.openai.com/v1/engines/text-davinci-003/completions'
        self.student_id=1001
        self.dataloader = Dataloader(student_id=self.student_id)
    def test_openai_api_call(self):
        # Define the prompt for the GPT-3.5 API

        dashboard_data = self.dataloader.get_dashboard_data(f"../data/dashboard/dash_board_data.json") \
            if os.path.exists(f"../data/dashboard/dash_board_data.json") else None
        DashB = pd.DataFrame(dashboard_data)
        prompt = "Summarize the following Pandas DataFrame:\n" + DashB.to_string() + "\nSummary:"
        # Set up the headers with the API key
        headers = {'Authorization': f'Bearer {self.api_key}'}

        # Set up the data payload for the API request
        data_payload = {'prompt': prompt, 'max_tokens': 250, 'temperature': 0.7}

        # Make a request to the OpenAI API
        response = requests.post(self.openai_endpoint, json=data_payload, headers=headers)

        # Assert that the API call was successful (status code 200)
        self.assertEqual(response.status_code, 200, f"API call failed with status code {response.status_code}")


#system testing code for checking if the chrome version are using appropriate

class TestChromeVersionCompatibility(unittest.TestCase):

    def test_chrome_version_compatibility(self):
        # Specify the expected Chrome version
        expected_chrome_version = '120.0.6099.71'  # Update this to the version you expect

        # Get the actual Chrome version
        actual_chrome_version = self.get_chrome_version()

        # Check if the actual version matches the expected version
        self.assertEqual(actual_chrome_version, expected_chrome_version,
                         f"Chrome version mismatch. Expected: {expected_chrome_version}, Actual: {actual_chrome_version}")

        # Additional tests or actions with the web application using selenium can be added here

    def get_chrome_version(self):
        # Use selenium to open Chrome and retrieve its version
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')  # Run Chrome in headless mode
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('chrome://version/')
            version_info = driver.find_element_by_xpath('//tr[td[contains(text(), "Chrome")]]/td[2]').text
            chrome_version = version_info.split(' ')[0]
            return chrome_version
        finally:
            driver.quit()



if __name__ == '__main__':
    unittest.main()
