
import json
import streamlit as st
import pandas as pd
# from view import View


class Model():

    def __init__(self, student_id):
        self.student_id = student_id
    def convert_piazzajson_to_csv(self, json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        title = []
        topic = []
        poster = []
        poster_date = []
        body = []
        body = []
        follow_up_1 = []
        follow_up_2 = []
        follow_up_3 = []
        follow_up_4 = []
        if isinstance(data, list):
            json_data = data[0]['Posts']
        else:
            json_data = data['Posts']
        for i in json_data:  # or data['Posts'] - for
            title.append(i['Title'])
            topic.append(i['Topic'])
            poster.append(i['Poster'])
            poster_date.append(i['Post Date'])
            body.append(i['Body'])
            follow_up_1.append(i['Followups'][0]['Body'])
            try:
                follow_up_2.append(i['Followups'][1]['Body'])
            except:
                follow_up_2.append(None)
            try:
                follow_up_3.append(i['Followups'][2]['Body'])
            except:
                follow_up_3.append(None)
            try:
                follow_up_4.append(i['Followups'][3]['Body'])
            except:
                follow_up_4.append(None)

        df = pd.DataFrame({
            'title': title,
            'topic': topic,
            'poster': poster,
            'poster_date': poster_date,
            'body': body,
            'follow_up_1': follow_up_1,
            'follow_up_2': follow_up_2,
            'follow_up_3': follow_up_3,
            'follow_up_4': follow_up_4
        })

        return df

    def get_moodle_data(self, json_file_path):

        keys_to_keep = ['Course Title', 'Course Syllabus', 'Grade Breakdown']

        with open(json_file_path, 'r') as file:
            data = json.load(file)

            # Filtered dictionary using a dictionary comprehension
        data_for_llm = {key: data[key] for key in keys_to_keep if key in data}

        if 'Assignments' in data:
            moodle_df = pd.DataFrame(data['Assignments']).T
        else:
            moodle_df = None
        if 'Grades' in data:
            summary_of_moodle_grade = pd.DataFrame(data['Grades']).describe().drop(index='count')
            score = pd.DataFrame(data['Grades']).T.filter([f'{self.student_id}'], axis=1) * 100
        else:
            summary_of_moodle_grade = None
            score = None

        return data_for_llm, moodle_df, summary_of_moodle_grade, score

    def get_grade_scope_data(self, json_file_path):

        with open(json_file_path, 'r') as file:
            data = json.load(file)
        # data = json.loads('./gradescope/math314.json')

        hws = pd.DataFrame(data['Assignments']).T

        stats = pd.DataFrame(data['Grades']).describe().drop(index='count')
        score = pd.DataFrame(data['Grades']).T.filter([f'{self.student_id}'], axis=1) * 100
        return hws, stats, score
