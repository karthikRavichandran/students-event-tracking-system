import streamlit as st
import sys
sys.path.append('../')
from ui.page import Page

class Moodle(Page):
    """
    The Page is the moodle page, which shows all the relevant moodle info for each course.

    ...

    Attributes
    ----------
    courses : List
        A list of courses which the student is enrolled in for display
    data : dict
        A dict representing a mapping from course name to course information from moodle for each class.

    Methods
    -------
    display()
        Displays the moodle webpage onto the screen for the student to see.
    display_course(data)
        Displays the given course information onto the screen.
    """

    def __init__(self, courses, data):
        """
        Parameters
        ----------
        courses : List
            A list of courses which the student is enrolled in for display
        data : dict
            A dict representing a mapping from course name to course information from moodle for each class.
        """
        self.courses = courses
        self.data = data

    def display(self):
        """Displays the moodle webpage onto the screen for the student to see."""
        for course in self.courses:
            st.subheader(f'_Class {course} Moodle_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')
            self.display_course(*self.data[course])

    def display_course(self, data_for_llm, moodle_df, summary_of_moodle_grade, score):
        """
        Displays the given course information onto the screen.

        Parameters
        ----------
        moodle_df : pandas.Dataframe
            The moodle information for this course
        score : pandas.Dataframe
            The raw grades this student got on gradescope
        """
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
