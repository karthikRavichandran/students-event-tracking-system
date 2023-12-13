import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
import random
import time
from ui.page import Page
from server.llm import generate_summary, get_prompts

class Dashboard(Page):

    def __init__(self):
        pass

    def display(self, ):
        DashB = pd.DataFrame({"Courses": ['math314', 'lang101', 'phys999', 'math314'],
                              "Description": ['HW1', 'Project Proposal', 'Quiz 3', 'Mid-Term'],
                              "Summary": ['Calculus and partial derivative', 'Understanding language syntax',
                                          'learning about escape velocity', 'Chapter 1 to Chapter 7'],
                              "Due in (days)": [3, 7, 4, 5],
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
        with st.spinner('Wait for AI output...'):
            time.sleep(60)
            txt = st.caption(f"{generate_summary(DashB, prompt_user=get_prompts(field='advice')[1])}")
        # st.caption(
        #     '''
        #     1. Math314: Make sure to allocate enough time to review the material from Chapter 1 to Chapter 7 (5 days) for the mid-term exam, as the critical level is quite high.
        #     2. Lang101: Spend time to brainstorm ideas and create a comprehensive project proposal as the critical level is low.
        #     3. Phys999: Spend time to review the material related to escape velocity (4 days) as the critical level is very high.
        #
        #     ''')

        st.subheader('_Important Piazza Discussion_  :blue[Summary] :coffee:', divider='rainbow')
        txt = st.caption(
            '''
            lang101 - Subject: Does anyone have insights or opinions on its definition in the readings we've covered so far?

            Discussion: Hello everyone! I've been pondering over the use of the word 'shall' in Old English texts. 
            It seems to carry different meanings in various contexts. Does anyone have insights or opinions on its definition in the readings we've covered so far?"'''
        )