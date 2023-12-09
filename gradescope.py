import streamlit as st
import pandas as pd
import random
from read_syntatic_data import get_grade_scope_data, get_moodle_data
def gradescope():
    student_id = 1003
    DashB2 = pd.DataFrame({"Event": ['CS520', 'CS646', 'CS670', 'CS520']*5,
                              "Description": ['HW1', 'Project Proposal', 'Quiz 3', 'Mid-Term']*5,
                              "Summary": ['Git commands and collaborations', 'Understanding LLM and project proposal',
                                          'Testing and Validation', 'Chapter 1 to Chapter 7']*5,
                              "Due in": [3, 7, 4, 5]*5,
                              "Avg. Scores (%)": ['89', '90', '78', '89']*5,
                              "Critical Level": ['High', 'Low', 'Very-High', 'Low']*5,
                              "Grade progress": [[random.randint(50, 100) for _ in range(10)] for _ in range(4*5)]})

    def gradescope_display(json_file_path = './data/gradescope/math314.json'):
        hws, stats, score = get_grade_scope_data(json_file_path, student_id = student_id)
        # c1, c2 = st.columns((2, 1))
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
            column_config = {str(student_id): "Your Score"},
            hide_index=False,
            width=2000,
            height=180
        )

    st.subheader('_Class MATH314 Grade scope_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')

    gradescope_display(json_file_path = './data/gradescope/math314.json')
    st.subheader('_Class PHYS999 Grade scope_  :green[Stats] :chart_with_upwards_trend:', divider='rainbow')
    gradescope_display(json_file_path='./data/gradescope/phys999.json')
    st.subheader('_Class LANG101 Grade scope_  :red[No Stats] :coffee:', divider='rainbow')
    st.caption('Check Moodle for this course')
    # gradescope_display(json_file_path='./data/gradescope/math314.json')



