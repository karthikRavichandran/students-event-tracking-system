import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
from ui.page import Page

class Gradescope(Page):

    def __init__(self, courses, data):
        self.courses = courses
        self.data = data

    def display(self):
        for course in self.courses:
            st.subheader(f'_Class {course} Gradescope_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')
            if self.data[course] is None:
                st.caption('Check Moodle for this course')
            else:
                self.display_course(*self.data[course])

    def display_course(self, hws, stats, score):
        st.caption('Homework Description and due date')
        st.dataframe(
                hws,
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
            pd.concat([stats.T, score], axis=1),
            column_config = {"TODO": "Your Score"},
            hide_index=False,
            width=2000,
            height=180
        )
