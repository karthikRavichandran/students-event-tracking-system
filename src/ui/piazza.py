import streamlit as st
import sys
sys.path.append('../')
# from server.llm import generate_summary, get_prompts
from ui.page import Page
from server.llm import generate_summary
import time

class Piazza(Page):

    def __init__(self, courses, dfs):
        self.courses = courses
        self.dfs = dfs

    def display(self):
        for course in self.courses:
            st.subheader(f'_Discussion from piazza for {course}_  :orange[TOP Discussions] :coffee:',divider='rainbow')
            self.display_course(self.dfs[course], course)
             # TODO

    def display_course(self, df, course):
        st.caption('Homework Description and due date')
        st.dataframe(
            df,
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
            height=20 * df.shape[0]
        )

        st.caption("AI Summary")
        with st.spinner('Wait for AI output...'):
            time.sleep(60)
            txt = st.caption(f"{generate_summary(df, prompt_user='Generate summary for top 3 post based on date and professor response. Give the summary in points')}")
        # self.piazza_LLM_sample_caption(course=course)
        # with c1:

    def piazza_LLM_sample_caption(self, course):
        if course == 'lang101':
            sample_caption = '''
                1. Poster Alice asked for excused absence from class due to illness and received a positive response from the professor.
                2. Poster Alice asked for clarification on Homework 1 Question 2 and received help from the professor and Bob.
                3. Poster Bob proposed forming a study group for the upcoming midterm exam and received positive responses from Alice and the professor.
                '''
            st.caption(
                sample_caption
            )

        if course == 'math314':
            sample_caption = '''
        General Course Questions: Alice kickstarted the semester by asking for general questions about the course content, schedule, and expectations. Bob asked about the balance between theory and application in the course, and the professor clarified that a balance between theory and application would be struck throughout the course, with an emphasis on practical applications.

        Homework 1 Tips and Tricks: Carol started a thread to exchange tips and tricks for Homework 1. Bob suggested breaking down the steps of the solution before diving in, and Carol recommended Khan Academy's videos on related rates.

        Midterm 1 Study Group Formation: Bob suggested forming a study group to review concepts and solve practice problems together. Alice and Carol both expressed interest in joining the group, and the professor encouraged them to coordinate their study group activities.
        '''
            st.caption(
                sample_caption
            )

        if course == 'phys999':
            sample_caption = st.caption(
        '''
        1. Comparing Lab1 and Lab2: Professor opened a discussion on the differences and unique aspects of Lab1 and Lab2, with Lab1 introducing foundational concepts in classical mechanics and Lab2 taking it up a notch with experiments in electromagnetism and optics. The labs are designed to complement each other, providing a holistic view of physics.
        2. Project Excitement: Professor opened a discussion on potential project ideas and the exciting possibilities that lie ahead. Alice is considering a project on quantum entanglement, Bob is leaning towards a project on astrophysics, and Carol is considering a project on renewable energy technologies. The diversity of topics showcases the breadth of physics.
        3. Midterm Exam Preparation Strategies: Professor discussed strategies for effective preparation for the midterm exam. Alice suggested creating a comprehensive study schedule and practicing past exam questions, Bob recommended group study sessions, and Carol suggested creating concept maps. Each student has a unique approach, so find what works best for them.
        4. Final Exam Countdown: Professor discussed final preparations for the final exam. Alice and Bob are struggling with certain concepts related to quantum mechanics, and Carol could use some extra practice with electromagnetism problems. For quantum mechanics, focus
        ''')
            st.caption(
                sample_caption
            )
