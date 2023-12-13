import streamlit as st
import sys
sys.path.append('../')
from ui.page import Page

class CourseInfo(Page):

    def __init__(self, courses, data):
        self.courses = courses
        self.data = data

    def display(self):
        option = st.selectbox('Select the course to view the details',self.courses, disabled=False)
        st.subheader(f'_Class {option} Information_', divider='rainbow')
        self.display_course(self.data[option])

    def display_course(self, data):
        description = data[0]
        st.caption(description["Course Title"])
        st.caption("Syllabus")
        st.markdown(description["Course Syllabus"])
        st.caption("Grade Breakdown")
        st.table(description["Grade Breakdown"])
