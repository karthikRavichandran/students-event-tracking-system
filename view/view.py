import streamlit as st
from read_syntatic_data import convert_piazzajson_to_csv
from model.model import Model
import random
import pandas as pd
class View:

    def __init__(self, student_id):
        self.student_id = student_id
        self.model = Model(self.student_id)

    def piazza_LLM_sample_caption(self, course):
        if course == 'LANG101':
            sample_caption = '''
                1. Poster Alice asked for excused absence from class due to illness and received a positive response from the professor.
                2. Poster Alice asked for clarification on Homework 1 Question 2 and received help from the professor and Bob.
                3. Poster Bob proposed forming a study group for the upcoming midterm exam and received positive responses from Alice and the professor.
                '''
            st.caption(
                sample_caption
            )

        if course == 'MATH314':
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

    def piazza_display(self,json_file_path='./data/piazza/lang101.json'):
        # json_file_path = './data/piazza/lang101.json'
        df = self.model.convert_piazzajson_to_csv(json_file_path)
        # c1, c2 = st.columns((2, 1))
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

        # txt = st.caption(f"{generate_summary(df, prompt_user='Generate summary for top 3 post based on date and professor response. Give the summary in points')}")
        st.caption("AI Summary")
        # with c1:

    def dashboard(self, ):
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

        # txt = st.caption(f"{generate_summary(DashB, prompt_user=get_prompts(field='advice')[1])}")
        st.caption(
            '''
            1. Math314: Make sure to allocate enough time to review the material from Chapter 1 to Chapter 7 (5 days) for the mid-term exam, as the critical level is quite high.
            2. Lang101: Spend time to brainstorm ideas and create a comprehensive project proposal as the critical level is low.
            3. Phys999: Spend time to review the material related to escape velocity (4 days) as the critical level is very high.
    
            ''')

        st.subheader('_Important Piazza Discussion_  :blue[Summary] :coffee:', divider='rainbow')
        txt = st.caption(
            '''
            lang101 - Subject: Does anyone have insights or opinions on its definition in the readings we've covered so far?

            Discussion: Hello everyone! I've been pondering over the use of the word 'shall' in Old English texts. 
            It seems to carry different meanings in various contexts. Does anyone have insights or opinions on its definition in the readings we've covered so far?"'''
        )

    def gradescope_display(self, json_file_path = './data/gradescope/math314.json'):
        hws, stats, score = self.model.get_grade_scope_data(json_file_path)
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
            column_config = {str(self.student_id): "Your Score"},
            hide_index=False,
            width=2000,
            height=180
        )