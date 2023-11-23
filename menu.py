import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
# import cv2
import pandas as pd
# from st_aggrid import AgGrid
# import plotly.express as px
import io
import random
import pandas as pd
import streamlit as st
from dashboard import dashboard
from alerts import alerts
from grade_piazza import grade_piazza

# st.set_page_config(layout="wide")

def menu():
    if 'choose' not in st.session_state:
        st.session_state['choose'] = None
    with st.sidebar:
        st.session_state['choose'] = option_menu("Student Event Tracker", ["Dashboard", "Alerts", "Grade/Piazza", "Course Info", "Contact"],
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
        dashboard()

    elif st.session_state['choose'] == 'Alerts':
        alerts()
    elif st.session_state['choose'] == 'Grade/Piazza':
        grade_piazza()
