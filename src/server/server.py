import streamlit as st
from database.dataloader import Dataloader
from ui.menu import Menu
from ui.gradescope import Gradescope
from ui.dashboard import Dashboard
from ui.piazza import Piazza
import os

class Server:
    
    def __init__(self, student_id):
        self.student_id = student_id
        self.dataloader = Dataloader(self.student_id)
        self.courses = ["lang101", "math314", "phys999"]
        self.menu = Menu()
        self.piazza_data = {course : 
                            (self.dataloader.get_piazza_df(f"../data/piazza/{course}.json") 
                             if os.path.exists(f"../data/piazza/{course}.json") else None)
                            for course in self.courses}
        self.gradescope_data = {course : 
                            (self.dataloader.get_gradescope_data(f"../data/gradescope/{course}.json") 
                             if os.path.exists(f"../data/gradescope/{course}.json") else None)
                            for course in self.courses}
        self.moodle_data = {course : 
                            (self.dataloader.get_moodle_data(f"../data/moodle/{course}.json") 
                             if os.path.exists(f"../data/moodle/{course}.json") else None)
                            for course in self.courses}
        self.piazza = Piazza(self.courses, self.piazza_data)
        self.gradescope = Gradescope(self.courses, self.gradescope_data)
        self.dashboard = Dashboard()

        self.menu.display()
        self.display_loop()

    def display_loop(self):
        if st.session_state['choose'] == "Dashboard":
            self.dashboard.display()
        elif st.session_state['choose'] == 'Gradescope':
            self.gradescope.display()
        elif st.session_state['choose'] == 'Piazza':
            self.piazza.display()
    