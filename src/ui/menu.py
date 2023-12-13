from streamlit_option_menu import option_menu
import sys
sys.path.append('../')
import streamlit as st
from ui.page import Page

# st.set_page_config(layout="wide")
class Menu(Page):

    def __init__(self):
        pass

    def display(self):
        if 'choose' not in st.session_state:
            st.session_state['choose'] = None
        with st.sidebar:
            st.session_state['choose'] = option_menu("Student Event Tracker", ["Dashboard", "Gradescope", "Piazza", "Course Info", "Contact"],
                                    icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                                    menu_icon="app-indicator", default_index=0,
                                    styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#05ab21"}, ##02ab21
                }
            )

        

