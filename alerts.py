import streamlit as st
import pandas as pd
import random
def alerts():
    DashB2 = pd.DataFrame({"Event": ['CS520', 'CS646', 'CS670', 'CS520']*5,
                              "Description": ['HW1', 'Project Proposal', 'Quiz 3', 'Mid-Term']*5,
                              "Summary": ['Git commands and collaborations', 'Understanding LLM and project proposal',
                                          'Testing and Validation', 'Chapter 1 to Chapter 7']*5,
                              "Due in": [3, 7, 4, 5]*5,
                              "Avg. Scores (%)": ['89', '90', '78', '89']*5,
                              "Critical Level": ['High', 'Low', 'Very-High', 'Low']*5,
                              "Grade progress": [[random.randint(50, 100) for _ in range(10)] for _ in range(4*5)]})

    st.dataframe(
            DashB2,
            column_config={
                "Done": st.column_config.CheckboxColumn(
                    "Done",
                    help="Select your **favorite** widgets",
                    default=False,
                ),
                "Event": "Event",
                "Description": "Description",
                "Summary": "Summary",
                "Due in": st.column_config.NumberColumn(
                    "Due in",
                    help="Number of stars on GitHub",
                    format="%d Days",
                ),
                "Avg. Scores": "Avg. Scores",
                "Critical Level": "Critical Level",
                "Grade progress": st.column_config.LineChartColumn(
                    "Grade progress", y_min=50, y_max=100
                ),

            },
            hide_index=True,
            width=2000,
            height=700
        )