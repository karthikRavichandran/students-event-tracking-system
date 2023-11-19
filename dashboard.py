import streamlit as st
import pandas as pd
import random
from llm import generate_summary, get_prompts
from alerts import alerts
def dashboard():
    DashB = pd.DataFrame({"Event": ['CS520', 'CS646', 'CS670', 'CS520'],
                          "Description": ['HW1', 'Project Proposal', 'Quiz 3', 'Mid-Term'],
                          "Summary": ['Git commands and collaborations', 'Understanding LLM and project proposal',
                                      'Testing and Validation', 'Chapter 1 to Chapter 7'],
                          "Due in": [3, 7, 4, 5],
                          "Avg. Scores (%)": ['89', '90', '78', '89'],
                          "Critical Level": ['High', 'Low', 'Very-High', 'Low'],
                          "Grade progress": [[random.randint(50, 100) for _ in range(10)] for _ in range(4)]})

    # Use the full page instead of a narrow central column

    # Space out the maps so the first one is 2x the size of the other three
    # c1, c2, c3, c4 = st.columns((2, 1, 1, 1))
    st.subheader('Analytics :chart_with_upwards_trend:')
    st.dataframe(
        DashB,
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
    )
    st.caption("For more alerts go to Alerts")
    if st.button("Alerts"):
        st.session_state.choose = 'Alerts'

    st.subheader('_Advice from AI_', divider='rainbow')


    # txt = st.caption(f"{generate_summary(DashB, prompt_user=get_prompts(field='advice')[1])}"
    #                  )
    st.caption(
    '''
    1. For CS520, focus on mastering git commands and collaborations in order to score high. Make sure to also study chapters 1 to 7 for the mid-term and aim for a low critical grade progress.

    2. For CS646, work on understanding LLM and developing your project proposal. Make sure the project proposal is well-crafted and aim for a low critical grade progress.

    3. For CS670, focus on learning the concepts of testing and validation in order to score high in the quiz. Make sure to aim for a very-high critical grade progress.
    ''')

    st.subheader('_Important Piazza Discussion_  :blue[Summary] :coffee:', divider='rainbow')
    txt = st.caption(
        '''
        CS 520 - Subject: More details about the expections for each of the 6 new test cases

        Discussion: It's is mention in Hints for homework 3, that 
            The second test case (add transaction fails its input validtion) may either be the Model or the View.
            The remaining 3 test cases may be the model, view, or controller.
            I am a bit confused now how can I test via model, do we need to pass a variable and set error message to it?
            Also can we get an aggregated post  which would describe what every unit test is expecting ie whether we are expected to test Model/View/Controller or any combination of them?'''
    )
