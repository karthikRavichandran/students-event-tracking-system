import streamlit as st
import sys
sys.path.append('../')
from ui.page import Page

class StudentInfo(Page):

    def __init__(self, data):
        self.data = data

    def display(self):
        st.table(self.data)
