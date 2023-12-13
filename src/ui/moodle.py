import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
from ui.page import Page

class Moodle(Page):

    def __init__(self, courses, data):
        self.courses = courses
        self.data = data

    def display(self):
        for course in self.courses:
            st.subheader(f'_Class {course} Moodle_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')
            self.display_course(*self.data[course])

    def display_course(self, data_for_llm, moodle_df, summary_of_moodle_grade, score):
        if score is None:
            st.text("Check Gradescope for this course")
            return
        st.caption('Homework Description and due date')
        st.dataframe(
                moodle_df,
                column_config={
                    "Done": st.column_config.CheckboxColumn(
                        "Done",
                        help="Select your **favorite** widgets",
                        default=False,
                    ),
                    "Title": "Title",
                    "Description": "Description",
                    # "index": "HW",
                    "Due Date": st.column_config.DateColumn(),

                },
                hide_index=False,
                width=2000,
                height=180
            )
        # with c1:
        st.caption('Your Grade summary and class stats')
        st.dataframe(
            score,
            hide_index=False,
            width=2000,
            height=180
        )
