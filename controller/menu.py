from streamlit_option_menu import option_menu
import sys
sys.path.append('../')
import streamlit as st
from model.gradescope import gradescope
from model.piazza import grade_piazza
from view.view import View

# st.set_page_config(layout="wide")


def menu():
    view = View(student_id=1001)
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

    if st.session_state['choose'] == "Dashboard":
        view.dashboard()

    elif st.session_state['choose'] == 'Gradescope':
        gradescope()
    elif st.session_state['choose'] == 'Piazza':
        # model = Model(student_id=1001)
        grade_piazza()
