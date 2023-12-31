import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
import time
from ui.page import Page
# from server.llm import generate_summary, get_prompts
from server.llm import llm

class Dashboard(Page):
    """
    The Page is the dashboard page, which shows a summary of all the materials for the student.

    ...

    Attributes
    ----------
    DashB: pandas.Dataframe
        This is the dashboard information for the student.

    Methods
    -------
    display()
        Displays the dashboard webpage onto the screen for the student to see.

    """

    def __init__(self, dashboard_data):
        """
        Parameters
        ----------
        dashboard_data : dict
            This is the dashboard information for the student.
        """
        self.DashB = pd.DataFrame(dashboard_data)
        self.llm = llm()


    def display(self):
        """Displays the dashboard webpage onto the screen for the student to see."""
        st.subheader('Analytics :chart_with_upwards_trend:')
        st.dataframe(
            self.DashB,
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
            time.sleep(30)
            txt = st.caption(f"{self.llm.generate_summary(self.DashB, prompt_user=self.llm.get_prompts(field='advice')[1])}")
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